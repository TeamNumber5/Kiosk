from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('', csrf_exempt(views.index), name='index'),
]

urlpatterns += [
    path('', include('django.contrib.auth.urls')),
]
