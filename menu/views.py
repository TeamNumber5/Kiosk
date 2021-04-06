from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ResetDB, logout, CreateProduct
from login.forms import CreateUser
from Kiosk.models import Employee, Active_Employee
from menu.models import Item
from login import helper as h
from . import view_support as support
import time
from django.views.decorators.csrf import csrf_exempt


def index(request):
    # attempt to authorize and get employee
    auth, employee = support.auth_fetch(request)
    # get context for page
    employee_info = support.get_employee_info(employee)



    if request.method == 'POST':
        # Button to clear the database
        if 'clear_db' in request.POST:

            form = ResetDB(request.POST)

            users = Employee.objects.all()

            # delete all users in employee table
            for user in users:
                user.delete()

            # Delete all users in active employee table
            users = Active_Employee.objects.all()
            for user in users:
                user.delete()

            #Log out of session
            support.logout(request,auth,employee)
            auth = False


        # remove active user from db, and remove auth
        if 'logout_click' in request.POST:
            support.logout(request,auth,employee)
            auth = False

    # Only renders menu if authed and restricts temporary user from accessing menu 
    if auth and not support.is_temp(auth):
        return render(request, 'index_menu.html', employee_info)
    else:
        return HttpResponseRedirect('/login')
    
@csrf_exempt
def productDetail(request):
    # attempt to authorize and get employee
    auth, employee = support.auth_fetch(request)
    # get context for page
    employee_info = support.get_employee_info(employee)

    if request.method == 'POST':

        # remove active user from db, and remove auth
        if 'logout_click' in request.POST:
            support.logout(request,auth,employee)
            auth = False


    if auth and not support.is_temp(auth):
       '''
       proof of concept code
       '''
       item = Item.objects.filter(item_id ="11111").first()
       context = support.get_context(employee_info, item)
       
       return render(request, 'productDetail.html', context)
    else:
        return HttpResponseRedirect('/login')

@csrf_exempt
def productListing(request):

    # attempt to authorize and get employee
    auth, employee = support.auth_fetch(request)
    # get context for page
    employee_info = support.get_employee_info(employee)

    if request.method == 'POST':

        # remove active user from db, and remove auth
        if 'logout_click' in request.POST:
            support.logout(request,auth,employee)
            auth = False
    

    if auth and not support.is_temp(auth):
       '''
       proof of concept code
       '''
       item = Item.objects.filter(item_id ="78703").first()
       print(item.photo)
       context = support.get_context(employee_info, item)
       print(context['photo'])
       
       return render(request, 'productListing.html', context)
    else:
        return HttpResponseRedirect('/login')

@csrf_exempt
def createProduct(request):
    auth, employee = support.auth_fetch(request)
    # get context for page
    employee_info = support.get_employee_info(employee)
    if request.method == 'POST':
        if 'logout_click' in request.POST:
            support.logout(request,auth,employee)
            auth = False

        elif 'create_product' in request.POST:
            form = CreateProduct(request.POST)
            support.create_new_product(form, request.FILES)

            pass

    if auth and not support.is_temp(auth):
       return render(request, 'createProduct.html', employee_info)
    else:
        return HttpResponseRedirect('/menu')
    

@csrf_exempt
def employeeDetail(request):
    # attempt to authorize and get employee
    auth, employee = support.auth_fetch(request)
    # get context for page
    context = support.get_employee_info(employee)

    # Adds a bit more context for the page for form
    # submission error checking
    context['no_users'] = 0
    context['valid_info'] = 1
    context['user_created'] = 0
    context['employee_id'] = support.get_new_id()


    # Back button that returns to menu, and restricts
    # temporary user from accessing
    if 'back' in request.POST and not support.is_temp(auth):
        return (HttpResponseRedirect('/menu/'))

    # POST to create user
    if 'create_click' in request.POST:     

        # Get the form with user information
        form = CreateUser(request.POST)
        # Try to create the user, when db is empty
        if (h.empty_db(context)):

           # If the DB is empty ensure role is set to
           # a management position.
            try:
                role = form['role'].value()
            except:
                role = ""

            # Delete the temporary user
            support.delete_tmp_user()

            # Ensure role is a manager and create user
            if role == 'GM' or role == 'SM':
                if(h.attempt_create_user(form,context)):
                    auth = False

            # Else the info is invalid
            else:
                context['valid_info'] = 0

        # If database is not full
        else:
            if(h.attempt_create_user(form,context)):
                context['user_created'] = 1

    if request.method == 'POST':
        # remove active user from db, and remove auth
        if 'logout_click' in request.POST:
            support.logout(request,auth,employee)
            auth = False
    
    if auth and support.creds(auth):
        return render(request, 'employeeDetail.html', context)
    elif auth and not support.creds(auth):
        return HttpResponseRedirect('/menu')
    else:
        return HttpResponseRedirect('/login')
    
