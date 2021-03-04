from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from .forms import ResetDB
from .forms import logout
from login.forms import CreateUser
from Kiosk.models import Employee
from Kiosk.models import Active_Employee
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

def index(request):
    # attempt to authorize and get employee
    auth, employee = auth_fetch(request)
    # get context for page
    employee_info = get_employee_info(employee)

    if request.method == 'POST':
        # Button to clear the database
        if 'clear_db' in request.POST:
            form = ResetDB(request.POST)
            users = Employee.objects.all()

            for user in users:
                user.delete()
            
            users = Active_Employee.objects.all()
            for user in users:
                user.delete()

            logout(request,auth,employee)
            auth = False


        # remove active user from db, and remove auth
        if 'logout_click' in request.POST:
            logout(request,auth,employee)
            auth = False

            
    if auth:
        return render(request, 'index_menu.html', employee_info)
    else:
        return HttpResponseRedirect('/login')
        
@csrf_exempt
def productListing(request):

    auth, employee = auth_fetch(request)
    employee_info = get_employee_info(employee)

    if request.method == 'POST':

        # remove active user from db, and remove auth
        if 'logout_click' in request.POST:
            logout(request,auth,employee)
            auth = False

    if auth:
       return render(request, 'productListing.html', employee_info)
    else:
        return HttpResponseRedirect('/login')
    

@csrf_exempt
def employeeDetail(request):
    auth, employee = auth_fetch(request)
    employee_info = get_employee_info(employee)
    context = { 'no_users' : 0, 'valid_info' : 1}


    if 'create_click' in request.POST:     
        # Get the form
        form = CreateUser(request.POST)
        # Try to create the user, if not context will change
        h.attempt_create_user(form,context)

    if request.method == 'POST':
        # remove active user from db, and remove auth
        if 'logout_click' in request.POST:
            logout(request,auth,employee)
            auth = False

    if auth:
       return render(request, 'employeeDetail.html', employee_info)
    else:
        return HttpResponseRedirect('/login')
    
