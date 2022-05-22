from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import auth, messages
from users.models import *
# Create your views here.

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']		
        x = auth.authenticate(email=email, password=password)		
        user = get_object_or_404(User, email=email)		
        #is_nurse = user.is_nurse
        if x is not None:
            auth.login(request, x)            
            return redirect('/profile')		
        else:
            print(email)
            print(password)
           
            messages.info(request, "invalid credentials")
            return redirect('/login')
    else:		
        return render(request, "login.html")

def logout_user(request):
    logout(request)
    return redirect('/login')
