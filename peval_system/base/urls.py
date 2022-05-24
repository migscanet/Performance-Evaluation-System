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

    path("edit_educ_att/<int:pk>/", views.edit_educ_att, name='edit_educ_att'),
    path("edit_workexp/<int:pk>/", views.edit_workexp, name='edit_workexp'),
    path("edit_acc_events/<int:pk>/", views.edit_acc_events, name='edit_acc_events'),
    path("edit_pub/<int:pk>/", views.edit_pub, name='edit_pub'),
    path("edit_res_grants/<int:pk>/", views.edit_res_grants, name='edit_res_grants'),
	path("edit_licexam/<int:pk>/", views.edit_licexam, name='edit_licexam'),
    path("edit_trainsem/<int:pk>/", views.edit_trainsem, name='edit_trainsem'),
    path("edit_confwork/<int:pk>/", views.edit_confwork, name='edit_confwork'),
    path("edit_extserv/<int:pk>/", views.edit_extserv, name='edit_extserv'),
    
    path("delete_educ_att/<int:pk>/", views.delete_educ_att, name='delete_educ_att'),
    path("delete_workexp/<int:pk>/", views.delete_workexp, name='delete_workexp'),
    path("delete_acc_events/<int:pk>/", views.delete_acc_events, name='delete_acc_events'),
    path("delete_pub/<int:pk>/", views.delete_pub, name='delete_pub'),
    path("delete_res_grants/<int:pk>/", views.delete_res_grants, name='delete_res_grants'),
    path("delete_licexam/<int:pk>/", views.delete_licexam, name='delete_licexam'),
    path("delete_trainsem/<int:pk>/", views.delete_trainsem, name='delete_trainsem'),
    path("delete_confwork/<int:pk>/", views.delete_confwork, name='delete_confwork'),
    path("delete_extserv/<int:pk>/", views.delete_extserv, name='delete_extserv'),
]

urlpatterns += static(settings.UPLOAD_URL, document_root=settings.UPLOAD_ROOT)
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.)