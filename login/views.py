from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from .forms import SubmitLogin
def index(request):

    if request.method == 'POST':

        form = SubmitLogin(request.POST)

        if (str(form['user_name'].value()) == 'user' and str(form['user_password'].value()) == 'password'):
            return HttpResponseRedirect('/menu/')
    else:
        form = SubmitLogin()
    
    return render(request, 'index.html') 

