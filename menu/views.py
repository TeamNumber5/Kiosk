from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ResetDB, logout, CreateProduct, UpdateProduct, GoUpdate, DeleteProduct
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
      # context = support.get_context(employee_info, item)
        
       
       return render(request, 'productDetail.html', context)
    else:
        return HttpResponseRedirect('/login')

@csrf_exempt
def productListing(request):

    # attempt to authorize and get employee
    auth, employee = support.auth_fetch(request)
    # get context for page
    context = support.get_employee_info(employee)

    # Back button that returns to menu, and restricts
    # temporary user from accessing
    if 'back' in request.POST and not support.is_temp(auth):
        return (HttpResponseRedirect('/menu/'))

    if request.method == 'POST':

        # remove active user from db, and remove auth
        if 'logout_click' in request.POST:
            support.logout(request,auth,employee)
            auth = False
        
        # Go's to create product page
        if 'go_create_new' in request.POST:
            try:
                del request.session['to_update'] 
            except:
                pass
            return HttpResponseRedirect('/productListing/createProduct')

        # Go's to create product page with product loaded to update
        if 'go_update' in request.POST:
            form = GoUpdate(request.POST)
            try:
                request.session['to_update'] = form['product_id'].value()
            except:
                context.update(support.get_all_items())
       
                return render(request, 'productListing.html', context)

            return HttpResponseRedirect('/productListing/createProduct')

    
    # If the user is authed render the page with context
    if auth and not support.is_temp(auth):
       context.update(support.get_all_items())
       
       return render(request, 'productListing.html', context)
    else:
        return HttpResponseRedirect('/login')

@csrf_exempt
def createProduct(request):
    auth, employee = support.auth_fetch(request)
    # get context for page
    employee_info = support.get_employee_info(employee)
    context = {}
    context['create_product'] = 0
    context['update_product'] = 0
    context['to_update'] = 0

    # Back button that returns to menu, and restricts
    # temporary user from accessing
    if 'back' in request.POST and not support.is_temp(auth):
        return (HttpResponseRedirect('/productListing/'))

    if request.method == 'POST':
        # Handles logout
        if 'logout_click' in request.POST:
            support.logout(request,auth,employee)
            auth = False

        # Handles create product
        elif 'create_product' in request.POST:
            form = CreateProduct(request.POST)
            if(support.create_new_product(form)):
                context['create_product'] = 1

        # handles update product
        elif 'update_product' in request.POST:
            form = UpdateProduct(request.POST)
            if(support.update_product(form)):
                context['update_product'] = 1
        # Deletes product 
        elif 'delete_product' in request.POST:
            form = DeleteProduct(request.POST)
            if(support.delete_product(form)):
                return (HttpResponseRedirect('/productListing/'))
    # if the user is authd
    if auth and not support.is_temp(auth):
        try:
            # Gets the item to update from teh user session
            to_update = request.session['to_update']
        except:
            # If there is no item to update get other context
            context.update(support.get_all_items())
            context.update(employee_info)
            return render(request, 'createProduct.html', context)
        try:
            # Get the item to updates information
            item  = Item.objects.get(item_id=to_update)
            item_wrap = {}
            load_item = []
            load_item.append(to_update)
            load_item.append(item.item_name)
            load_item.append(float(item.item_price))
            load_item.append(item.item_description)
            load_item.append(item.item_available)
            item_wrap['to_update'] = load_item
            context.update(item_wrap)
            context.update(support.get_all_items())
            context.update(employee_info)
        except:
            pass

        return render(request, 'createProduct.html', context)

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
                if(h.attempt_create_user(form,context)): # Initial user create
                    auth = False
                    

            # Else the info is invalid
            else:
                context['valid_info'] = 0

        # If database is not full
        else:
            if(h.attempt_create_user(form,context)):
                context['user_created'] = 1
                context['new_gen_id'] = support.get_last_created_id()# Saves ID to be displayed

                

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



