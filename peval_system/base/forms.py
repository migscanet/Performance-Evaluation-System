from django import forms
from .models import *

class EducAttForm(forms.ModelForm):
    class Meta:
        model = EducationalAttainment
        #exclude = ('blood_requisition_request',)
        exclude = ['user', 'is_approved', 'is_verified', 'comments_remarks' ]

class WorkExpForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        #exclude = ('blood_requisition_request',)
        exclude = ['user', 'is_approved', 'is_verified', 'comments_remarks']

class AccEventsForm(forms.ModelForm):
    class Meta:
        model = AccomplishmentsEvents
        #exclude = ('blood_requisition_request',)
        exclude = ['user', 'is_approved', 'is_verified', 'comments_remarks', 'date_created']

class PubForm(forms.ModelForm):
    class Meta:
        model = Publications
        #exclude = ('blood_requisition_request',)
        exclude = ['user', 'is_approved', 'is_verified', 'comments_remarks']

class ResearchGrantsForm(forms.ModelForm):
    class Meta:
        model = ResearchGrants
        #exclude = ('blood_requisition_request',)
        exclude = ['user', 'is_approved', 'is_verified', 'comments_remarks']

class LicExamForm(forms.ModelForm):
    class Meta:
        model = LicensureExam
        #exclude = ('blood_requisition_request',)
        exclude = ['user', 'is_approved', 'is_verified', 'comments_remarks']

class TrainSemForm(forms.ModelForm):
    class Meta:
        model = TrainingSeminars
        #exclude = ('blood_requisition_request',)
        exclude = ['user', 'is_approved', 'is_verified', 'comments_remarks']

class ConfWorkForm(forms.ModelForm):
    class Meta:
        model = ConferenceWorkshops
        #exclude = ('blood_requisition_request',)
        exclude = ['user', 'is_approved', 'is_verified', 'comments_remarks']

class ExtServForm(forms.ModelForm):
    class Meta:
        model = ExtensionServices
        #exclude = ('blood_requisition_request',)
        exclude = ['user', 'is_approved', 'is_verified', 'comments_remarks']

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


