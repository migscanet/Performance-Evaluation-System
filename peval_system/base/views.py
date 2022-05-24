from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import auth, messages
from django.contrib.auth.forms import UserCreationForm
from .models import *

#Admin Functionalities

@login_required(login_url='/login',)
def create_account():
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("User created successfully!")
    else:
        form = UserCreationForm()
        return render(request, 'auth/create_user.html', {'form': form})


# @login_required(login_url='/login',)
def update_faculty_info():
    print()

# @login_required(login_url='/login',)
def update_FSR():
    print()

# @login_required(login_url='/login',)
def update_SET():
    print()

