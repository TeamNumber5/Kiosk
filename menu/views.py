from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ResetDB
from Kiosk.models import Employee
from Kiosk.models import Active_Employee
# Create your views here.

def index(request):
    auth = False
    try:
        session_key = request.session.get('session_key')
        if session_key:    
            auth = Active_Employee.objects.filter(session_key=request.session['session_key']).first()
    except:
        pass


    if request.method == 'POST':

        form = ResetDB(request.POST)

        if 'clear_db' in request.POST:
            users = Employee.objects.all()

            for user in users:
                user.delete()

            
    if auth:
        return render(request, 'index_menu.html')
    else:
        return HttpResponseRedirect('/login/')

def productListing(request):
    return render(request, 'productListing.html')

def employeeDetail(request):
    return render(request, 'employeeDetail.html')
