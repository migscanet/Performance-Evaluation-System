from dataclasses import fields
from django import forms
from .models import *
from users.models import *
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from datetime import date
from crispy_forms.helper import FormHelper


# class CreateUserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         exclude = ['is_active']
#     def save(self, commit=True):
#         user = super(CreateUserForm, self).save(commit=False)
#         user.is_active = True
#         if commit:
#             user.save()
#         return user

class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    class Meta:

        model = User

        exclude = ['is_active', 'last_login', 'date_joined', 'is_Faculty']
        labels = {
            'email': 'Email:',
            # 'alternative_email': 'Alternative Email:',
            'first_name': 'First Name:', 
            'last_name': 'Last Name:', 
            'middle_name': 'Middle Name:',
            'suffix': 'Suffix:',
            'sex': 'Sex:',
            'birth_date': 'Birth Date:',
            'birth_place': 'Birth Place:',
            'present_address': 'Present Address:',
            'permanent_address': 'Permanent Address:',
            'civil_status': 'Civil Status:',
            'religion': 'Religion:',
            'profile_photo': 'Profile Photo:',
            'phone_number': 'Phone Number:',
            'landline_number': 'Landline Number:',
            'emergency_contact_name': 'Emergency Contact Name:',
            'emergency_contact_number': 'Emergency Contact Number:',
            'emergency_contact_birthdate': 'Emergency Contact Birthdate:',
            'emergency_contact_relationship': 'Emergency Contact Relationship:',
            'department': 'Department:',
            'faculty_rank': 'Faculty Rank:',
            'faculty_classification': 'Faculty Classification:',
            'faculty_tenure': 'Faculty Tenure:',
            'faculty_status': 'Faculty Status:',
            'role': 'Role:',
        }

        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'example@mail.com', 'autofocus': True}),
            'phone_number': forms.TextInput(attrs={'placeholder': '09123456789','type':'number'}),
            'landline_number': forms.TextInput(attrs={'placeholder': '09123456789','type':'number'}),
            'emergency_contact_number': forms.TextInput(attrs={'placeholder': '09123456789','type':'number'}),
            # 'birth_date': DateInput(),
            # 'emergency_contact_birthdate': DateInput(),
            }

    #Form validation on the email field
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            user = User.objects.exclude(pk=self.instance.pk).get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % user)

    # def clean_alternative_email(self):
    #     alternative_email = self.cleaned_data['alternative_email'].lower()
    #     try:
    #         user = User.objects.exclude(pk=self.instance.pk).get(alternative_email=alternative_email)
    #     except User.DoesNotExist:
    #         return alternative_email
    #     raise forms.ValidationError('Alternative Email "%s" is already in use.' % user)

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
        exclude = ['user', 'is_approved', 'is_verified', 'comments_remarks']


