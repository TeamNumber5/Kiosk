from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from .forms import SubmitLogin
from django.contrib.auth import authenticate, login
def index(request):

    if request.method == 'POST':

        form = SubmitLogin(request.POST)
        user = authenticate(username=str(form['user_name'].value()), password=str(form['user_password'].value()))
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/menu/')
    
    return render(request, 'index.html') 

