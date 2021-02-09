from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from Kiosk.models import Employee

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
            user_name =str(form['user_name'].value())
            user_password= str(form['user_password'].value())

            # if either are empty 
            if not user_name or not user_password:
                return render(request, 'index.html') 


            # Query for the login info 
            login = Employee.objects.filter(employee_id=user_name,  password=user_password).first()

            if login:
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
            employee.save()
 
    return render(request, 'index.html') 
