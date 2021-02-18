from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from Kiosk.models import Employee
from Kiosk.models import Active_Employee

import random
import string

# Create your views here.
from .forms import SubmitLogin
from .forms import CreateUser


def index(request):
    # Request is type post
    with open('users.txt', 'w') as user:
        users = Employee.objects.all()
        for item in users:
            print ('-' * 40, file=user)
            print ('first_name '.ljust(15, ' ') + str(item.first_name),file=user)
            print ('last_name '.ljust(15, ' ') + str(item.last_name),file=user)
            print ('employee_id '.ljust(15, ' ') + str(item.employee_id),file=user)
            print ('password '.ljust(15, ' ') + str(item.password), file=user)
            print ('role '.ljust(15, ' ') + str(item.role),  file=user)

    if request.method == 'POST':
        
        if 'login_click' in request.POST:
            # Login form
            form = SubmitLogin(request.POST)
            # Login info
            try:
                employee_id =int(str(form['employee_id'].value()))
                user_password= str(form['user_password'].value())
            except:
                print('Logon error')
                return
            
            if employee_id == None or user_password == None:
                return render(request, 'index.html') 


            # Query for the login info 
            login = Employee.objects.filter(employee_id=employee_id,  password=user_password).first()

            # If a user is found assign him to his old session or create a new active user session
            if login:
                session_key = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
                name = login.first_name
                employee_id = login.employee_id
                role = login.role
               
                """
                This is just checking to see if user is already logged in and didn't log out
                """
                logged_in = Active_Employee.objects.filter(employee_id=employee_id).first()

                if logged_in:
                    request.session['session_key'] = logged_in.session_key
                    return HttpResponseRedirect('/menu/')
                
                active_employee = Active_Employee.objects.create(employee_id=employee_id, name=name, role=role, session_key=session_key)
                active_employee.save()

                request.session['session_key'] = session_key
                # If so direct them to the menu
                return HttpResponseRedirect('/menu/')


        # on create account  click, create the account if the user is not found
        elif 'create_click' in request.POST:     
            form = CreateUser(request.POST)

            first_name =str(form['first_name'].value())
            last_name = str(form['last_name'].value())
            user_password= str(form['user_password'].value())
            
            employee_id = int(form['employee_id'].value())
            
            role = str(form['role'].value())

            employee = Employee.objects.create(first_name=first_name,last_name=last_name, employee_id=employee_id, password=user_password, role=role)
            
            if role == 'GM' or role == 'SM':
                employee.manager = employee_id

            employee.save()
 
    return render(request, 'index.html') 
