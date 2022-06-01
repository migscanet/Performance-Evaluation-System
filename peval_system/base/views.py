from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, HttpRequest
from django.template import loader
from django.contrib import auth, messages
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import ROLECHOICES
from .models import *
from .forms import *
from users.forms import AddClerkForm
import xlwt

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

def admin_dash(request):
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
    create_user_form = CreateUserForm()
    educ_form = EducAttForm()
    work_exp_form = WorkExpForm()
    acc_events_form = AccEventsForm()
    pub_form = PubForm()
    research_grants_form = ResearchGrantsForm()
    lic_exam_form = LicExamForm()
    train_sem_form = TrainSemForm()
    conf_work_form = ConfWorkForm()
    ext_serv_form = ExtServForm()
    faculty_serv_rec_form = FacultyServRecForm()


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
        'create_user_form': create_user_form,
        'educ_form': educ_form,
        'work_exp_form': work_exp_form,
        'acc_events_form': acc_events_form,
        'pub_form': pub_form,
        'research_grants_form': research_grants_form,
        'lic_exam_form': lic_exam_form,
        'train_sem_form': train_sem_form,
        'conf_work_form': conf_work_form,
        'ext_serv_form': ext_serv_form,
        'faculty_serv_rec_form': faculty_serv_rec_form
    }
    return render(request, 'admin_dash.html', context)

def add_user(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    
    form = CreateUserForm()
    return render(request, 'add_user.html', {'form': form})

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

def edit_user(request, pk):
    entry = get_object_or_404(User, pk=pk)

    if request.method == "POST":
        tempForm = CreateUserForm(request.POST, request.FILES, instance = entry)
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
                # INCLUDE EDIT USER HTML
        return render(request, 'update_user.html', context)
  
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

# UNIT HEAD FUNCTIONALITIES
def unit_dash_view(request):
    user = User.objects.get(id=request.user.id)

    if(user.is_UnitHead == True):
        return render(request, 'unithead_dashboard.html')
    return render(request, 'unithead_dashboard.html')

def unit_table_view(request):
    user = User.objects.get(id=request.user.id)
    accomplishments = AccomplishmentsEvents.objects.all()

    if(user.is_UnitHead == True):
        context = {
            'accomplishments': accomplishments  
        }
    return render(request, 'unithead_dashboard_table.html', context)

def unit_faculty_view(request):
    user = User.objects.get(id=request.user.id)
    users = User.objects.all()

    if(user.is_UnitHead == True):
        context = {
            'users': users
        }

        return render(request, 'unithead_faculty_list.html', context)

def unit_approval_view(request):
    user = User.objects.get(id=request.user.id)
    if(user.is_UnitHead == True):
        return render(request, 'unithead_pending_approvals.html')

def unit_assignment_view(request):
    user = User.objects.get(id=request.user.id)
    users = User.objects.all()

    if(user.is_UnitHead == True):
        context = {
            'users': users
        }

        return render(request, 'unithead_role_assignment.html', context)

# DEPT CHAIR FUNCTIONALITIES
def dept_dash_view(request):
    user = User.objects.get(id=request.user.id)

    if(user.is_DepartmentHead == True):
        return render(request, 'deptchair_dashboard.html')
    return render(request, 'deptchair_dashboard.html')

def dept_table_view(request):
    user = User.objects.get(id=request.user.id)
    accomplishments = AccomplishmentsEvents.objects.all()

    if(user.is_DepartmentHead == True):
        context = {
            'accomplishments': accomplishments  
        }
    return render(request, 'deptchair_dashboard_table.html', context)

def dept_faculty_view(request):
    user = User.objects.get(id=request.user.id)
    users = User.objects.all()

    if(user.is_DepartmentHead == True):
        context = {
            'users': users
        }

        return render(request, 'deptchair_faculty_list.html', context)

def dept_approval_view(request):
    user = User.objects.get(id=request.user.id)
    if(user.is_DepartmentHead == True):
        return render(request, 'deptchair_pending_approvals.html')

def dept_assignment_view(request):
    user = User.objects.get(id=request.user.id)
    users = User.objects.all()

    if(user.is_DepartmentHead == True):
        context = {
            'users': users
        }

        return render(request, 'deptchair_role_assignment.html', context)

def dept_clerk_view(request):
    user = User.objects.get(id=request.user.id)
    
    if user:    
        if request.method == "POST":
            addclerkform = AddClerkForm(request.POST)

            if addclerkform.is_valid():
                instance = addclerkform.save(commit=False)	
                instance.save()
                instance.role = ROLECHOICES[3]
                instance.save()
                #message.success(request, "")
                print('valid')
                return redirect('/profile')
            else:
                print('not valid')
                #message.error(request, "Failed.")
                pass
            context = {}
            context['form'] = AddClerkForm()
            template = loader.get_template('deptchair_add_clerk.html')
            return HttpResponse(template.render(context, request))
        else:
            print('not post')
            form = AddClerkForm()
            return render(request, 'deptchair_add_clerk.html', {'form': form})
    else:
        print('not user')
        form = AddClerkForm()
        return render(request, 'deptchair_add_clerk.html', {'form': form})

def export_excel_accom(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Accomplishment.xls"'

    wb = xlwt.Workbook(encoding='utf-8') 
    ws = wb.add_sheet('Export')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    #accType = accom_choices(AccomplishmentsEvents.objects.('type'))

    column = ['user', 'first_name', 'last_name', 'accomplishment title','description', 'type', 'start date', 'date ended']

    for col_num in range(len(column)):
        ws.write(row_num, col_num, column[col_num], font_style)

    font_style = xlwt.XFStyle()

    #name = User.get(pk=1) 

    rows = AccomplishmentsEvents.objects.all().values_list('user','user_id__first_name','user_id__last_name', 'type', 'description', 'type','start_date', 'end_date'  )
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)

    return response



