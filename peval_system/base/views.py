from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.contrib import auth, messages
from .forms import GenericLoginForm
from .models import AddEducationalAttainment, AddWorkExperience, AddAccomplishmentsEvents, AddPublications, AddTrainingSeminars, AddResearchGrants, AddLicensureExam, AddConferenceWorkshops, AddExtensionServices, FacultyServiceRecord
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

import sys

# sys.path.append("/Laptop Files/eval_sys_128.2/Performance-Evaluation-System/peval_system/users")
# from users.models import User, FacultyProfile

# from peval_system.users.models import UserManager, User, FacultyProfile


def index(request):
    """
    Landing page
    """
    template = loader.get_template('PES_login.html')
    context = {}
    context['form'] = GenericLoginForm()
    return HttpResponse(template.render(context, request))

def change_password(request):
    template = loader.get_template('PES_change_password.html')
    context = {}
    return HttpResponse(template.render(context, request))

# def faculty_login(request):
#     if request.method == 'POST':
        #form = GenericLoginForm(request.POST)
        # if form.is_valid():
        #     username = request.POST['username']
        #     password = request.POST['password']
        #     user = authenticate(request, username=username, password=password)
        #     if user is not None:
        #         user_type = User.objects.filter(user=user)
        #         print("user ok. at extended lookup now: ", len(user_type))
        #         if len(User)>=1:
        #             print("is faculty? ", user_type[0].is_Faculty)
        #             if user_type[0].is_Faculty:
        #                 #get approval status
        #                 faculty_obj = User.objects.get(user=user)
        #                 approved = faculty_obj.is_approved
        #                 if approved:
        #                     login(request, user)
        #                     messages.success(request, "Patient Login Sucess!")
        #                     return redirect(index)
        # print("Invalid login")
        # pass
    # template = loader.get_template('patient_login.html')
    # context = {}
    # context['form'] = GenericLoginForm()
    # return HttpResponse(template.render(context, request))