<<<<<<< HEAD
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

# @login_required(login_url='/login',)
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

=======
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import auth, messages
from .models import *
from .forms import *

# Create your views here.
def view_profile(request):
    educ_att = EducationalAttainment.objects.all()
    work_exp = WorkExperience.objects.all()
    acc_event = AccomplishmentsEvents.objects.all()
    pubs = Publications.objects.all()
    research_grants = ResearchGrants.objects.all()
    lic_exams = LicensureExam.objects.all()
    train_sem = TrainingSeminars.objects.all()
    conf_work = ConferenceWorkshops.objects.all()
    ext_serv = ExtensionServices.objects.all()
    faculty_serv_rec = FacultyServiceRecord.objects.all()

    #myFilter = RequestFilter(request.GET, queryset=requests)
    #request = myFilter.qs

    context = {
        'EducAtt' : educ_att,
        'WorkExp' : work_exp,   
        'AccEvent' : acc_event,
        'Pub' : pubs,   
        'ResGrant' : research_grants,
        'LicExam' : lic_exams,   
        'TrainSem' : train_sem,
        'ConfWork' : conf_work,    
        'ExtServ' : ext_serv,    
        'FacServRec' : faculty_serv_rec,    
    }

    return render(request, 'profile.html', context)
    

def add_educ_att(request):
    user = User.objects.get(id=request.user.id)
    
    if user:    
        print(user)
        if request.method == "POST":
            educattform = EducAttForm(request.POST, request.FILES)

            if educattform.is_valid():
                instance = educattform.save(commit=False)	
                instance.user = user
                instance.save()
                #message.success(request, "")
                print('valid')
                return redirect('/profile')
            else:
                print('not valid')
                #message.error(request, "Failed.")
                pass
            context = {}
            context['form'] = EducAttForm()
            template = loader.get_template('add_cred.html')
            return HttpResponse(template.render(context, request))
        else:
            print('not post')
            form = EducAttForm()
            return render(request, 'add_cred.html', {'form': form})
    else:
        print('not user')
        form = EducAttForm()
        return render(request, 'add_cred.html', {'form': form})

def add_workexp(request):
    user = User.objects.get(id=request.user.id)
    
    if user:    
        print(user)
        if request.method == "POST":
            workexpform = WorkExpForm(request.POST, request.FILES)

            if workexpform.is_valid():
                instance = workexpform.save(commit=False)	
                instance.user = user
                instance.save()
                #message.success(request, "")
                print('valid')
                return redirect('/profile')
            else:
                print('not valid')
                #message.error(request, "Failed.")
                pass
            context = {}
            context['form'] = WorkExpForm()
            template = loader.get_template('add_cred.html')
            return HttpResponse(template.render(context, request))
        else:
            print('not post')
            form = WorkExpForm()
            return render(request, 'add_cred.html', {'form': form})
    else:
        print('not user')
        form = WorkExpForm()
        return render(request, 'add_cred.html', {'form': form})

def add_acc_events(request):
    user = User.objects.get(id=request.user.id)
    
    if user:    
        print(user)
        if request.method == "POST":
            tempform = AccEventsForm(request.POST, request.FILES)

            if tempform.is_valid():
                instance = tempform.save(commit=False)	
                instance.user = user
                instance.save()
                #message.success(request, "")
                print('valid')
                return redirect('/profile')
            else:
                print('not valid')
                #message.error(request, "Failed.")
                pass
            context = {}
            context['form'] = AccEventsForm()
            template = loader.get_template('add_cred.html')
            return HttpResponse(template.render(context, request))
        else:
            print('not post')
            form = AccEventsForm()
            return render(request, 'add_cred.html', {'form': form})
    else:
        print('not user')
        form = AccEventsForm()
        return render(request, 'add_cred.html', {'form': form})

def add_pub(request):
    user = User.objects.get(id=request.user.id)
    
    if user:    
        print(user)
        if request.method == "POST":
            tempform = PubForm(request.POST, request.FILES)

            if tempform.is_valid():
                instance = tempform.save(commit=False)	
                instance.user = user
                instance.save()
                #message.success(request, "")
                print('valid')
                return redirect('/profile')
            else:
                print('not valid')
                #message.error(request, "Failed.")
                pass
            context = {}
            context['form'] = PubForm()
            template = loader.get_template('add_cred.html')
            return HttpResponse(template.render(context, request))
        else:
            print('not post')
            form = PubForm()
            return render(request, 'add_cred.html', {'form': form})
    else:
        print('not user')
        form = PubForm()
        return render(request, 'add_cred.html', {'form': form})


def add_res_grants(request):
    user = User.objects.get(id=request.user.id)
    
    if user:    
        print(user)
        if request.method == "POST":
            tempform = ResearchGrantsForm(request.POST, request.FILES)

            if tempform.is_valid():
                instance = tempform.save(commit=False)	
                instance.user = user
                instance.save()
                #message.success(request, "")
                print('valid')
                return redirect('/profile')
            else:
                print('not valid')
                #message.error(request, "Failed.")
                pass
            context = {}
            context['form'] = ResearchGrantsForm()
            template = loader.get_template('add_cred.html')
            return HttpResponse(template.render(context, request))
        else:
            print('not post')
            form = ResearchGrantsForm()
            return render(request, 'add_cred.html', {'form': form})
    else:
        print('not user')
        form = ResearchGrantsForm()
        return render(request, 'add_cred.html', {'form': form})  

def add_licexam(request):
    user = User.objects.get(id=request.user.id)
    
    if user:    
        print(user)
        if request.method == "POST":
            tempform = LicExamForm(request.POST, request.FILES)

            if tempform.is_valid():
                instance = tempform.save(commit=False)	
                instance.user = user
                instance.save()
                #message.success(request, "")
                print('valid')
                return redirect('/profile')
            else:
                print('not valid')
                #message.error(request, "Failed.")
                pass
            context = {}
            context['form'] = LicExamForm()
            template = loader.get_template('add_cred.html')
            return HttpResponse(template.render(context, request))
        else:
            print('not post')
            form = LicExamForm()
            return render(request, 'add_cred.html', {'form': form})
    else:
        print('not user')
        form = LicExamForm()
        return render(request, 'add_cred.html', {'form': form})  

def add_trainsem(request):
    user = User.objects.get(id=request.user.id)
    
    if user:    
        print(user)
        if request.method == "POST":
            tempform = TrainSemForm(request.POST, request.FILES)

            if tempform.is_valid():
                instance = tempform.save(commit=False)	
                instance.user = user
                instance.save()
                #message.success(request, "")
                print('valid')
                return redirect('/profile')
            else:
                print('not valid')
                #message.error(request, "Failed.")
                pass
            context = {}
            context['form'] = TrainSemForm()
            template = loader.get_template('add_cred.html')
            return HttpResponse(template.render(context, request))
        else:
            print('not post')
            form = TrainSemForm()
            return render(request, 'add_cred.html', {'form': form})
    else:
        print('not user')
        form = TrainSemForm()
        return render(request, 'add_cred.html', {'form': form})  

def add_confwork(request):
    user = User.objects.get(id=request.user.id)
    
    if user:    
        print(user)
        if request.method == "POST":
            tempform = ConfWorkForm(request.POST, request.FILES)

            if tempform.is_valid():
                instance = tempform.save(commit=False)	
                instance.user = user
                instance.save()
                #message.success(request, "")
                print('valid')
                return redirect('/profile')
            else:
                print('not valid')
                #message.error(request, "Failed.")
                pass
            context = {}
            context['form'] = ConfWorkForm()
            template = loader.get_template('add_cred.html')
            return HttpResponse(template.render(context, request))
        else:
            print('not post')
            form = ConfWorkForm()
            return render(request, 'add_cred.html', {'form': form})
    else:
        print('not user')
        form = ConfWorkForm()
        return render(request, 'add_cred.html', {'form': form})  

def add_extserv(request):
    user = User.objects.get(id=request.user.id)
    
    if user:    
        print(user)
        if request.method == "POST":
            tempform = ExtServForm(request.POST, request.FILES)

            if tempform.is_valid():
                instance = tempform.save(commit=False)	
                instance.user = user
                instance.save()
                #message.success(request, "")
                print('valid')
                return redirect('/profile')
            else:
                print('not valid')
                #message.error(request, "Failed.")
                pass
            context = {}
            context['form'] = ExtServForm()
            template = loader.get_template('add_cred.html')
            return HttpResponse(template.render(context, request))
        else:
            print('not post')
            form = ExtServForm()
            return render(request, 'add_cred.html', {'form': form})
    else:
        print('not user')
        form = ExtServForm()
        return render(request, 'add_cred.html', {'form': form})  
  
def edit_educ_att(request, pk):
    entry = get_object_or_404(EducationalAttainment, pk=pk)
    
    if request.method == "POST":
        #print('post')
        tempForm = EducAttForm(request.POST, request.FILES, instance=entry)
        if tempForm.is_valid():
            print('valid')       
            instance = tempForm.save(commit=False)           
            instance.save()
            messages.success(request, "Changes saved successfully!")       
            return redirect("/profile")                    
        else:
            messages.error(request, "Unsuccessful")
    else:
        print('not post?')
        tempForm = EducAttForm(instance=entry)
        context = {
                'tempForm':tempForm,		
                }
        return render(request, 'edit_cred.html', context)

def edit_workexp(request, pk):
    entry = get_object_or_404(WorkExperience, pk=pk)
    
    if request.method == "POST":
        #print('post')
        tempForm = WorkExpForm(request.POST, request.FILES, instance=entry)
        if tempForm.is_valid():
            print('valid')       
            instance = tempForm.save(commit=False)           
            instance.save()
            messages.success(request, "Changes saved successfully!")       
            return redirect("/profile")                    
        else:
            messages.error(request, "Unsuccessful")
    else:
        print('not post?')
        tempForm = WorkExpForm(instance=entry)
        context = {
                'tempForm':tempForm,		
                }
        return render(request, 'edit_cred.html', context)

def edit_acc_events(request, pk):
    entry = get_object_or_404(AccomplishmentsEvents, pk=pk)
    
    if request.method == "POST":
        #print('post')
        tempForm = AccEventsForm(request.POST, request.FILES, instance=entry)
        if tempForm.is_valid():
            print('valid')       
            instance = tempForm.save(commit=False)           
            instance.save()
            messages.success(request, "Changes saved successfully!")       
            return redirect("/profile")                    
        else:
            messages.error(request, "Unsuccessful")
    else:
        print('not post?')
        tempForm = AccEventsForm(instance=entry)
        context = {
                'tempForm':tempForm,		
                }
        return render(request, 'edit_cred.html', context)

def edit_pub(request, pk):
    entry = get_object_or_404(Publications, pk=pk)
    #co_author = get_object_or_404(User, pk=pk)
    
    if request.method == "POST":
        #print('post')
        tempForm = PubForm(request.POST, request.FILES, instance=entry)
        if tempForm.is_valid():
            print('valid')       
            instance = tempForm.save(commit=False)    
            #instance.co_author_DPSM.set() = co_author
            instance.save()
            messages.success(request, "Changes saved successfully!")       
            return redirect("/profile")                    
        else:
            messages.error(request, "Unsuccessful")
    else:
        print('not post?')
        tempForm = PubForm(instance=entry)
        context = {
                'tempForm':tempForm,		
                }
        return render(request, 'edit_cred.html', context)

def edit_res_grants(request, pk):
    entry = get_object_or_404(ResearchGrants, pk=pk)
    
    if request.method == "POST":
        #print('post')
        tempForm = ResearchGrantsForm(request.POST, request.FILES, instance=entry)
        if tempForm.is_valid():
            print('valid')       
            instance = tempForm.save(commit=False)           
            instance.save()
            messages.success(request, "Changes saved successfully!")       
            return redirect("/profile")                    
        else:
            messages.error(request, "Unsuccessful")
    else:
        print('not post?')
        tempForm = ResearchGrantsForm(instance=entry)
        context = {
                'tempForm':tempForm,		
                }
        return render(request, 'edit_cred.html', context)

def edit_licexam(request, pk):
    entry = get_object_or_404(LicensureExam, pk=pk)
    
    if request.method == "POST":
        #print('post')
        tempForm = LicExamForm(request.POST, request.FILES, instance=entry)
        if tempForm.is_valid():
            print('valid')       
            instance = tempForm.save(commit=False)           
            instance.save()
            messages.success(request, "Changes saved successfully!")       
            return redirect("/profile")                    
        else:
            messages.error(request, "Unsuccessful")
    else:
        print('not post?')
        tempForm = LicExamForm(instance=entry)
        context = {
                'tempForm':tempForm,		
                }
        return render(request, 'edit_cred.html', context)

def edit_trainsem(request, pk):
    entry = get_object_or_404(TrainingSeminars, pk=pk)
    
    if request.method == "POST":
        #print('post')
        tempForm = TrainSemForm(request.POST, request.FILES, instance=entry)
        if tempForm.is_valid():
            print('valid')       
            instance = tempForm.save(commit=False)           
            instance.save()
            messages.success(request, "Changes saved successfully!")       
            return redirect("/profile")                    
        else:
            messages.error(request, "Unsuccessful")
    else:
        print('not post?')
        tempForm = TrainSemForm(instance=entry)
        context = {
                'tempForm':tempForm,		
                }
        return render(request, 'edit_cred.html', context)

def edit_confwork(request, pk):
    entry = get_object_or_404(ConferenceWorkshops, pk=pk)
    
    if request.method == "POST":
        #print('post')
        tempForm = ConfWorkForm(request.POST, request.FILES, instance=entry)
        if tempForm.is_valid():
            print('valid')       
            instance = tempForm.save(commit=False)           
            instance.save()
            messages.success(request, "Changes saved successfully!")       
            return redirect("/profile")                    
        else:
            messages.error(request, "Unsuccessful")
    else:
        print('not post?')
        tempForm = ConfWorkForm(instance=entry)
        context = {
                'tempForm':tempForm,		
                }
        return render(request, 'edit_cred.html', context)

def edit_extserv(request, pk):
    entry = get_object_or_404(ExtensionServices, pk=pk)
    
    if request.method == "POST":
        #print('post')
        tempForm = ExtServForm(request.POST, request.FILES, instance=entry)
        if tempForm.is_valid():
            print('valid')       
            instance = tempForm.save(commit=False)           
            instance.save()
            messages.success(request, "Changes saved successfully!")       
            return redirect("/profile")                    
        else:
            messages.error(request, "Unsuccessful")
    else:
        print('not post?')
        tempForm = ExtServForm(instance=entry)
        context = {
                'tempForm':tempForm,		
                }
        return render(request, 'edit_cred.html', context)

def delete_educ_att(request, pk):
    EducationalAttainment.objects.filter(pk=pk).delete()
    return redirect('/profile')

def delete_workexp(request, pk):
    WorkExperience.objects.filter(pk=pk).delete()
    return redirect('/profile')

def delete_acc_events(request, pk):
    AccomplishmentsEvents.objects.filter(pk=pk).delete()
    return redirect('/profile')

def delete_pub(request, pk):
    Publications.objects.filter(pk=pk).delete()
    return redirect('/profile')

def delete_res_grants(request, pk):
    ResearchGrants.objects.filter(pk=pk).delete()
    return redirect('/profile')

def delete_licexam(request, pk):
    LicensureExam.objects.filter(pk=pk).delete()
    return redirect('/profile')

def delete_trainsem(request, pk):
    TrainingSeminars.objects.filter(pk=pk).delete()
    return redirect('/profile')

def delete_confwork(request, pk):
    ConferenceWorkshops.objects.filter(pk=pk).delete()
    return redirect('/profile')

def delete_extserv(request, pk):
    ExtensionServices.objects.filter(pk=pk).delete()
    return redirect('/profile')


>>>>>>> d655bb4b763119d03bf45f6346477afa881f40f6
