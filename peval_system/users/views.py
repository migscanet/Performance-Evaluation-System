from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import auth, messages
from users.models import *
from .forms import *
# Create your views here.

def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')		
        x = auth.authenticate(email=email, password=password)		
        user = get_object_or_404(User, email=email)		
        
        
        #role = user.get_role_display
        role = user.role
        print(role)
        #is_faculty = user.is_Faculty
        #is_unithead = user.is_UnitHead
        #is_depthead = user.is_DepartmentHead
        if x is not None:
            print("not none")
            if role == "1": #Faculty
                print(role)
                auth.login(request, x)
                return redirect('/profile')	
            elif role == "4": #Admin Clerk
                print(role)
                auth.login(request, x)
                return redirect('/admin_dash')
            else:
                return render(request, "login2.html")
            #elif is_unithead == True:
                auth.login(request, x)
                return redirect('/unit_head_dash')
            #elif is_depthead == True:
                auth.login(request, x)
                return redirect('/dept_head_dash')
        else:
            print(email)
            print(password)
           
            messages.info(request, "invalid credentials")
            return redirect('/login')
    else:		
        return render(request, "login2.html")

def logout_user(request):
    logout(request)
    return redirect('/login')

def create_user(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            print('valid')
            return redirect('/admin_dash')
        else:
            print('not valid')
            form = UserUpdateForm()
            context = {
            'form':form,		
            }
            return render(request, 'create_user.html', context)
    else:
            print('not valid')
            form = UserUpdateForm()
            context = {
            'form':form,		
            }
            return render(request, 'create_user.html', context)


