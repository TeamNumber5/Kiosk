from django.shortcuts import render, redirect
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
        if auth.employee_id == 99999:
            return True
    except:
        pass
    return False

def get_employee_info(employee):
    employee_info = {'first_name' : 'temp', 'last_name' : 'temp', 'employee_id' : 99999, 'role' : 'GM'}
    
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
        if (user.employee_id == 99999):
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
