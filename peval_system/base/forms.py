from django import forms
from .models import *


class EducAttForm(forms.ModelForm):
    class Meta:
        model = EducationalAttainment
        #exclude = ('blood_requisition_request',)
        exclude = ['user', 'is_approved', 'is_verified', 'comments_remarks' ]
        widgets = {
            'start_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'end_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }

class WorkExpForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        #exclude = ('blood_requisition_request',)
        exclude = ['user', 'is_approved', 'is_verified', 'comments_remarks']
        widgets = {
            'start_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'end_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }

class AccEventsForm(forms.ModelForm):
    class Meta:
        model = AccomplishmentsEvents
        #exclude = ('blood_requisition_request',)
        exclude = ['user', 'is_approved', 'is_verified', 'comments_remarks', 'date_created']
        widgets = {
            'start_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'end_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }

class PubForm(forms.ModelForm):
    class Meta:
        model = Publications
        #exclude = ('blood_requisition_request',)
        exclude = ['user', 'is_approved', 'is_verified', 'comments_remarks']
        widgets = {
            'date_published': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }

class ResearchGrantsForm(forms.ModelForm):
    class Meta:
        model = ResearchGrants
        #exclude = ('blood_requisition_request',)
        exclude = ['user', 'is_approved', 'is_verified', 'comments_remarks']
        widgets = {
            'project_start_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'project_end_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'actual_start_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'actual_end_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }

class LicExamForm(forms.ModelForm):
    class Meta:
        model = LicensureExam
        #exclude = ('blood_requisition_request',)
        exclude = ['user', 'is_approved', 'is_verified', 'comments_remarks']
        widgets = {
            'date_exam': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }

class TrainSemForm(forms.ModelForm):
    class Meta:
        model = TrainingSeminars
        #exclude = ('blood_requisition_request',)
        exclude = ['user', 'is_approved', 'is_verified', 'comments_remarks']
        widgets = {
            'start_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'end_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }

class ConfWorkForm(forms.ModelForm):
    class Meta:
        model = ConferenceWorkshops
        #exclude = ('blood_requisition_request',)
        exclude = ['user', 'is_approved', 'is_verified', 'comments_remarks']
        widgets = {
            'start_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'end_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'presentation_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }

class ExtServForm(forms.ModelForm):
    class Meta:
        model = ExtensionServices
        #exclude = ('blood_requisition_request',)
        exclude = ['user', 'is_approved', 'is_verified', 'comments_remarks']
        widgets = {
            'date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }

class FacultyServRecForm(forms.ModelForm):
    class Meta:
        model = FacultyServiceRecord
        #exclude = ('blood_requisition_request',)
        exclude = ['set', 'user', 'is_approved', 'comments_remarks']

class ClerkFacultyServRecForm(forms.ModelForm):
    class Meta:
        model = FacultyServiceRecord
        #exclude = ('blood_requisition_request',)
        exclude = ['set', 'is_approved', 'comments_remarks']


class SETForm(forms.ModelForm):
    class Meta:
        model = FacultyServiceRecord
        #exclude = ('blood_requisition_request',)
        fields = ['set']


