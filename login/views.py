from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from Kiosk.models import Employee

# Create your views here.
from .forms import SubmitLogin


def index(request):
    # Request is type post
    if request.method == 'POST':

        # Gets the form
        form = SubmitLogin(request.POST)
        user_name =str(form['user_name'].value())
        user_password= str(form['user_password'].value())

        # if either are empty 
        if not user_name or not user_password:
            return render(request, 'index.html') 


        # Query for the login info 
        login = Employee.objects.filter(first_name=user_name,  password=user_password).first()


        # on login click attempt to login
        if 'login_click' in request.POST:
                if login:
                    # If so direct them to the menu
                    return HttpResponseRedirect('/menu/')


        # on create account  click, create the account if the user is not found
        elif 'create_click' in request.POST and not login:     
                employee = Employee.objects.create(first_name=user_name, password=user_password)
                employee.save()
 
    return render(request, 'index.html') 
