from django.contrib import admin
from django.urls import path, include 
from . import views
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve



app_name = 'base'

urlpatterns =[
    path("profile", views.view_profile, name='view_profile'),
    path("add_educ_att", views.add_educ_att, name='add_educ_att'),
    path("add_workexp", views.add_workexp, name='add_workexp'),
    path("add_pub", views.add_pub, name='add_pub'),
    path("add_acc_events", views.add_acc_events, name='add_acc_events'),
    path("add_res_grants", views.add_res_grants, name='add_res_grants'),
    path("add_licexam", views.add_licexam, name='add_licexam'),
    path("add_trainsem", views.add_trainsem, name='add_trainsem'),
    path("add_confwork", views.add_confwork, name='add_confwork'),
    path("add_extserv", views.add_extserv, name='add_extserv'),
	
]

urlpatterns += static(settings.UPLOAD_URL, document_root=settings.UPLOAD_ROOT)
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.)