from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from .forms import ResetDB
from .forms import logout
from Kiosk.models import Employee
from Kiosk.models import Active_Employee
# Create your views here.


def authAndFetch(request,auto,employee_info):
    auth = False
    try:
        session_key = request.session.get('session_key')
        if session_key:
                auth = Active_Employee.objects.filter(session_key=request.session['session_key']).first()
                employee = Employee.objects.filter(employee_id=auth.employee_id).first()
                first_name = employee.first_name
                last_name = employee.last_name
                employee_id = employee.employee_id
                role = employee.role
                employee_info = {'first_name' : first_name, 'last_name' : last_name, 'employee_id' : employee_id, 'role' : role}
    except:
        pass

def index(request):
    auth = False
    try:
        session_key = request.session.get('session_key')
        if session_key:
                auth = Active_Employee.objects.filter(session_key=request.session['session_key']).first()
                employee = Employee.objects.filter(employee_id=auth.employee_id).first()
                first_name = employee.first_name
                last_name = employee.last_name
                employee_id = employee.employee_id
                role = employee.role
                employee_info = {'first_name' : first_name, 'last_name' : last_name, 'employee_id' : employee_id, 'role' : role}
    except:
        pass
    if request.method == 'POST':


        if 'clear_db' in request.POST:
            form = ResetDB(request.POST)
            users = Employee.objects.all()

            for user in users:
                user.delete()
            
            users = Active_Employee.objects.all()
            for user in users:
                user.delete()
            try:
                del request.session['session_key']
                auth.delete()
                auth = False
            except:
                pass

        if 'logout_click' in request.POST:
            try:
                del request.session['session_key']
                auth.delete()
                auth = False
            except:
                pass

            
    if auth:
        return render(request, 'index_menu.html', employee_info)
    else:
        return HttpResponseRedirect('/login')

def productListing(request):
    auth = False
    employee_info = {}
    authAndFetch(request,auth,employee_info)
    if auth:
        return render(request, 'productListing.html')
    else:
        return HttpResponseRedirect('/login')

def employeeDetail(request):
    return render(request, 'employeeDetail.html')
