from django.contrib import admin
from django.urls import path, include 
from . import views
from django.conf.urls import url
from django.urls import path
from .views import *



app_name = 'users'

urlpatterns =[
	# path("", index, name='index'),
	path("login", login, name='login'),
]