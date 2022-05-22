from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
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
            template = loader.get_template('add_educ_att.html')
            return HttpResponse(template.render(context, request))
        else:
            print('not post')
            form = EducAttForm()
            return render(request, 'add_educ_att.html', {'form': form})
    else:
        print('not user')
        form = EducAttForm()
        return render(request, 'add_educ_att.html', {'form': form})

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
            template = loader.get_template('add_workexp.html')
            return HttpResponse(template.render(context, request))
        else:
            print('not post')
            form = WorkExpForm()
            return render(request, 'add_workexp.html', {'form': form})
    else:
        print('not user')
        form = WorkExpForm()
        return render(request, 'add_workexp.html', {'form': form})

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
            template = loader.get_template('add_acc_events.html')
            return HttpResponse(template.render(context, request))
        else:
            print('not post')
            form = AccEventsForm()
            return render(request, 'add_acc_events.html', {'form': form})
    else:
        print('not user')
        form = AccEventsForm()
        return render(request, 'add_acc_events.html', {'form': form})

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
            template = loader.get_template('add_pub.html')
            return HttpResponse(template.render(context, request))
        else:
            print('not post')
            form = PubForm()
            return render(request, 'add_pub.html', {'form': form})
    else:
        print('not user')
        form = PubForm()
        return render(request, 'add_pub.html', {'form': form})


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
            template = loader.get_template('add_res_grants.html')
            return HttpResponse(template.render(context, request))
        else:
            print('not post')
            form = ResearchGrantsForm()
            return render(request, 'add_res_grants.html', {'form': form})
    else:
        print('not user')
        form = ResearchGrantsForm()
        return render(request, 'add_res_grants.html', {'form': form})  

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
            template = loader.get_template('add_licexam.html')
            return HttpResponse(template.render(context, request))
        else:
            print('not post')
            form = LicExamForm()
            return render(request, 'add_licexam.html', {'form': form})
    else:
        print('not user')
        form = LicExamForm()
        return render(request, 'add_licexam.html', {'form': form})  

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
            template = loader.get_template('add_trainsem.html')
            return HttpResponse(template.render(context, request))
        else:
            print('not post')
            form = TrainSemForm()
            return render(request, 'add_trainsem.html', {'form': form})
    else:
        print('not user')
        form = TrainSemForm()
        return render(request, 'add_trainsem.html', {'form': form})  

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
            template = loader.get_template('add_confwork.html')
            return HttpResponse(template.render(context, request))
        else:
            print('not post')
            form = ConfWorkForm()
            return render(request, 'add_confwork.html', {'form': form})
    else:
        print('not user')
        form = ConfWorkForm()
        return render(request, 'add_confwork.html', {'form': form})  

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
            template = loader.get_template('add_extserv.html')
            return HttpResponse(template.render(context, request))
        else:
            print('not post')
            form = ExtServForm()
            return render(request, 'add_extserv.html', {'form': form})
    else:
        print('not user')
        form = ExtServForm()
        return render(request, 'add_extserv.html', {'form': form})  
  
