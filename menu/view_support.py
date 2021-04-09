from django.shortcuts import render, redirect
import os
import random
import string
import copy
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ResetDB, logout
from login.forms import CreateUser
from Kiosk.models import Employee, Active_Employee
from menu.models import Item
from login import helper as h
import time
from django.views.decorators.csrf import csrf_exempt


'''
Authorizes request and returns employee associated with 
that specific request
'''
def auth_fetch(request):
    auth = False
    employee = False
    try:
        # get the generated session key if there is one
        session_key = request.session['session_key']
        if session_key:
            # Search for the session key in the active user table
            auth = Active_Employee.objects.filter(session_key=session_key).first()
            employee = Employee.objects.filter(employee_id=auth.employee_id).first()
    except:
        pass
    return auth, employee

def creds(auth):
    cred = False
    try:
        if auth.role == "GM" or auth.role == "SM":
            cred = True
    except:
        pass
    return cred

def is_temp(auth):
    try:
        if auth.employee_id == "99999":
            return True
    except:
        pass
    return False

def get_new_id():
    employee_id = ''.join(random.choice(string.digits) for i in range(5))
    matched = Employee.objects.filter(employee_id=employee_id).first()
    while matched != None:
        employee_id = ''.join(random.choice(string.digits) for i in range(5))
        matched = Employee.objects.filter(employee_id=employee_id).first()

    return employee_id


# Returns the most recently created employee ID in the db
def get_last_created_id():
    createdEmployee = Employee.objects.latest('record_id')
    return createdEmployee.employee_id


'''
Creates a new product
'''
def create_new_product(form):
    # generate new ID unique id
    item_id = ''.join(random.choice(string.digits) for i in range(5))
    matched = Item.objects.filter(item_id=item_id).first()
    while matched != None:
        item_id = ''.join(random.choice(string.digits) for i in range(5))
        matched = Item.objects.filter(item_id=item_id).first()

    # get the information from the form
    info = {}
    try:
       name = str(form['product_name'].value())
       desc = str(form['product_desc'].value())
       price = float(form['product_price'].value())
       qavail = int(form['product_qavail'].value())
       
    except:
        print("failed")
        return False
    # Create the object from the form information
    item = Item.objects.create(item_id=item_id, item_name=name, item_price=price, item_description=desc, item_available=qavail)
    item.save()
    return True

'''
Updates and existing item
'''
def update_product(form):
    # Get the information from the form
    try:
       item_id = str(form['product_id'].value())
       name = str(form['product_name'].value())
       desc = str(form['product_desc'].value())
       price = float(form['product_price'].value())
       qavail = int(form['product_qavail'].value())
    except:
        print("failed")
        return False
    # Get the object, update, save
    item  = Item.objects.get(item_id=item_id)
    item.item_name = name
    item.item_description = desc
    item.item_price = price
    item.item_available = qavail
    item.save()
    return True

'''
deletes an existing product
'''
def delete_product(form):
    # Try to get the infromation from the form
    try:
       item_id = str(form['product_id'].value())
       item  = Item.objects.get(item_id=item_id)
       item.delete()
    except:
        print("failed")
        return False

    return True
'''
Gets all of the items
'''
def get_all_items():
    # Get all the items from the database
    items = Item.objects.all()
    all_items = {}
    context = []
    for item in items: 
        product = []
        product.append(item.item_id)
        product.append(item.item_name)
        product.append(float(item.item_price))
        product.append(item.item_description)
        product.append(item.item_available)
        context.append(copy.deepcopy(product))
    all_items['products'] = context
    return all_items


def get_employee_info(employee):
    employee_info = {'first_name' : 'temp', 'last_name' : 'temp', 'employee_id' : "99999", 'role' : 'GM'}
    
    try:
        first_name = employee.first_name
        last_name = employee.last_name
        employee_id = employee.employee_id
        role = employee.role
        employee_info = {'first_name' : first_name, 'last_name' : last_name, 'employee_id' : employee_id, 'role' : role}
    except:
        print("fail")
        pass
    return employee_info

def delete_tmp_user():
    users = Active_Employee.objects.all()
    for user in users:
        if (user.employee_id == "99999"):
            user.delete()

def logout(request, auth, employee):
    try:
        request.session.clear()
        auth.delete()
        employee.active = False
    except:
        pass

def create_user():
    pass
