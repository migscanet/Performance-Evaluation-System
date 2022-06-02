from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from django.contrib.auth.forms import UserCreationForm

class DateInput(forms.DateInput):
    input_type = 'date'

class PersonalInfoForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)        

    class Meta:

        model = User

        exclude = ['password1', 'password2', 'password', 'is_active', 'last_login', 'date_joined', 'role', 
            'is_Faculty', 'is_superuser', 'groups', 'department',
            'user_permissions', 'password', 'is_staff', 'is_UnitHead',
            'is_DepartmentHead', 'is_Admin', 'is_Faculty','faculty_rank', 'faculty_classification', 'faculty_tenure', 'faculty_status']

        widgets = {            
            'phone_number': forms.TextInput(attrs={'placeholder': '09123456789','type':'number'}),
            'landline_number': forms.TextInput(attrs={'placeholder': '09123456789','type':'number'}),
            'emergency_contact_number': forms.TextInput(attrs={'placeholder': '09123456789','type':'number'}),
            'birth_date': DateInput(),
            'emergency_contact_birthdate': DateInput(),
            }

class UserUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
    
    class Meta:

        model = User
        exclude = ['password']
        fields = ['first_name', 'middle_name', 'last_name', 'suffix', 'email', 'alternative_email', 'faculty_rank', 'department', 'faculty_classification', 'faculty_tenure', 'faculty_status']

        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'example@mail.com', 'autofocus': True}),
            'alternative_email': forms.TextInput(attrs={'placeholder': 'example@mail.com', 'autofocus': True}),
            
            }

class AddClerkForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    class Meta:

        model = User
        exclude = ['password']
        fields = ['first_name', 'last_name', 'email', 'alternative_email', 'password']
     