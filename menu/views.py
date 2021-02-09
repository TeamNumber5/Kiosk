from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ResetDB
from Kiosk.models import Employee
# Create your views here.

def index(request):
    if request.method == 'POST':

        form = ResetDB(request.POST)

        if 'clear_db' in request.POST:
            users = Employee.objects.all()

            for user in users:
                user.delete()

            

    return render(request, 'index_menu.html')
