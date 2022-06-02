from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import auth, messages
from users.models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from base.decorators import allowed_users
from django.contrib.auth.models import Group
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
            if role == "2" or user.is_UnitHead == True: #Unit Head
                print(role)
                auth.login(request, x)
                return redirect('/unithead_dashboard')
            elif role == "3" or user.is_DepartmentHead == True: #Dept Chair
                print(role)
                auth.login(request, x)
                return redirect('/deptchair_dashboard')
            elif role == "4" or user.is_Admin == True: #Admin Clerk
                print(role)
                auth.login(request, x)
                return redirect('/admin_dash')
            elif role == "1" or user.is_Faculty == True: #Faculty 
                print(role)
                auth.login(request, x)
                return redirect('/profile')	
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

@login_required(login_url='/login',)
@allowed_users(allowed_roles=['admin'])
def create_user(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            print('valid')
            admin_group = Group.objects.get(name='faculty') 
            admin_group.user_set.add(form)
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
            


