from django.contrib import admin
from django.urls import path, include 
from . import views
#from django.conf.urls import url
from django.urls import path
from .views import *



app_name = 'users'

urlpatterns =[
	path("", views.login, name='login'),
	path("login", views.login, name='login'),
	path('logout', views.logout_user, name='logout_user'),
]