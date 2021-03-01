from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from Kiosk.models import Employee
from Kiosk.models import Active_Employee
from . import helper as h
import json

import random
import string

# Create your views here.
from .forms import SubmitLogin
from .forms import CreateUser

def index(request):

    h.create_usertxt()
    # Request is type post
    context = { 'no_users' : 0, 'valid_info' : 1, 'invalid_login' : 'none' }

    if request.method == 'POST':
        # on create account  click, create the account if the user is not found
        if 'create_click' in request.POST:     
            # Get the form
            form = CreateUser(request.POST)

            # Try to create the user, if not context will change
            h.attempt_create_user(form,context)


        if 'login_click' in request.POST:
            # Login form
            form = SubmitLogin(request.POST)
            employee_id = 0
            user_password = ""
            # Login info
            try:
                employee_id =int(str(form['employee_id'].value()))
                user_password= str(form['user_password'].value())
            except:
                print('Logon error')
            

            # Query for the login info 
            user = h.get_user(employee_id, user_password)
            if(h.attempt_login(request,user,context)):
                return HttpResponseRedirect('/menu/')

    h.empty_db(context)
    

    return render(request, 'index.html', context) 
