from django.shortcuts import render, redirect
import os
import random
import string
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ResetDB, logout
from login.forms import CreateUser
from Kiosk.models import Employee, Active_Employee
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

def get_context(employee_info,item):
    context = {"item_id": 'null', "item_name": 'null', "item_price": "null", "item_description": "null", "photo": "null"}
    print(item)
    try:
        item_id = item.item_id
        item_name = item.item_name
        item_price = item.item_price
        item_description = item.item_description
        photo = item.photo
        context = {"item_id": item_id, "item_name": item_name, "item_price": item_price, "item_description": item_description, "photo": photo}
    except:
        print("caught")
        pass
    context.update(employee_info)
    return context

def get_new_id():
    employee_id = ''.join(random.choice(string.digits) for i in range(5))
    matched = Employee.objects.filter(employee_id=employee_id).first()
    while matched != None:
        employee_id = ''.join(random.choice(string.digits) for i in range(5))
        matched = Employee.objects.filter(employee_id=employee_id).first()

    return employee_id

def create_new_product(form):
    info = {}
    img = True
    try:
       info['name'] = form['name'].value()
       info['desc'] = form['desc'].value()
       info['price'] = float(form['price'].value())
       info['qavail'] = int(form['qavail'].value())
       try:
           info['img'] = form['img'].value()
       except:
           img = False
    except:
        return False

    if img:



    
    


def get_employee_info(employee):
    employee_info = {'first_name' : 'temp', 'last_name' : 'temp', 'employee_id' : "99999", 'role' : 'GM'}
    
    try:
        first_name = employee.first_name
        last_name = employee.last_name
        employee_id = employee.employee_id
        role = employee.role
        employee_info = {'first_name' : first_name, 'last_name' : last_name, 'employee_id' : employee_id, 'role' : role}
    except:
        pass
    return employee_info

def delete_tmp_user():
    users = Active_Employee.objects.all()
    for user in users:
        if (user.employee_id == "99999"):
            user.delete()

def logout(request, auth, employee):
    try:
        del request.session['session_key']
        auth.delete()
        employee.active = False
    except:
        pass

def create_user():
    pass
