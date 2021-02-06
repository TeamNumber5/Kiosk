from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'index_menu.html')
