from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import auth, messages
from users.models import *
# Create your views here.

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']		
        x = authenticate(email=email, password=password)
        print(x)		
        user = get_object_or_404(User, email=email)		
        #is_nurse = user.is_nurse
        is_admin = user.is_Admin
        is_faculty = user.is_Faculty
        is_unithead = user.is_UnitHead
        is_depthead = user.is_DepartmentHead

    
        if x is not None:
            if is_faculty == True:
                auth.login(request, x)
                return redirect('/profile')	
            elif is_admin == True:
                auth.login(request, x)
                return redirect('/admin_dash')
            elif is_unithead == True:
                auth.login(request, x)
                return redirect('/unit_head_dash')
            elif is_depthead == True:
                auth.login(request, x)
                return redirect('/dept_head_dash')
        else:
            # print(email)
            # print(password)
        
            messages.info(request, "invalid credentials")
            return redirect('/login')
    else:		
        return render(request, "login.html")

def logout_user(request):
    logout(request)
    return redirect('/login')
