from django.urls import path, include

#from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('change_password/',views.change_password, name='change_password'),
    path('index', views.index, name='index'),
    path('faculty_login/', views.faculty_login, name='faculty_login'),

    #---STAFF URLS---#
    path('staff/base/', views.staff_base),
    path('staff/add_faculty/', views.staff_add_faculty),
    path('staff/faculty_load/', views.staff_add_faculty_load),
]

#if settings.DEBUG:
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)