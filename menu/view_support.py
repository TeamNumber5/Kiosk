from django.shortcuts import render, redirect
import os
import random
import string
import copy
from PIL import Image
import PIL
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
'''
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
'''

def get_new_id():
    employee_id = ''.join(random.choice(string.digits) for i in range(5))
    matched = Employee.objects.filter(employee_id=employee_id).first()
    while matched != None:
        employee_id = ''.join(random.choice(string.digits) for i in range(5))
        matched = Employee.objects.filter(employee_id=employee_id).first()

    return employee_id

def create_new_product(form, img):
    try:
        img = img['product_img']
    except:
        img= None
    item_id = ''.join(random.choice(string.digits) for i in range(5))
    matched = Item.objects.filter(item_id=item_id).first()
    while matched != None:
        item_id = ''.join(random.choice(string.digits) for i in range(5))
        matched = Item.objects.filter(item_id=item_id).first()
    print(item_id)
    info = {}
    try:
       name = str(form['product_name'].value())
       print(name)
       desc = str(form['product_desc'].value())
       print(desc)
       price = float(form['product_price'].value())
       print(price)
       qavail = int(form['product_qavail'].value())
       print(qavail)
       
    except:
        print("failed")
        return False

    if img != None:
        img = Image.open(img)
        path = "/static/product_photos/{}.jpg".format(name)
        img.save(path)
        item = Item.objects.create(item_id=item_id, item_name=name, item_price=price, item_description=desc, item_available=qavail, photo=path)
        item.save()
    else:
        item = Item.objects.create(item_id=item_id, item_name=name, item_price=price, item_description=desc, item_available=qavail)
        item.save()
    return True


def update_product(form, img):
    try:
        img = img['product_img']
    except:
        img= None
    try:
       item_id = str(form['product_id'].value())
       name = str(form['product_name'].value())
       print(name)
       desc = str(form['product_desc'].value())
       print(desc)
       price = float(form['product_price'].value())
       print(price)
       qavail = int(form['product_qavail'].value())
       print(qavail)
    except:
        print("failed")
        return False
    item  = Item.objects.get(item_id=item_id)
    item.item_name = name
    item.item_description = desc
    item.item_price = price
    item.item_available = qavail
    if img != None:
        img = Image.open(img)
        path = "/static/product_photos/{}.jpg".format(name)
        img.save(path)
        item.photo = path
    else:
        item.photo = 'null'
    item.save()
    return True





def get_all_items():
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
        product.append(item.photo)
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
        del request.session['session_key']
        auth.delete()
        employee.active = False
    except:
        pass

def create_user():
    pass
