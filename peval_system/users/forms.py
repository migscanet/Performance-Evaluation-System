from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from django.contrib.auth.forms import UserCreationForm

class PersonalInfoForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)        

    class Meta:

        model = User

        exclude = ['password', 'is_active', 'last_login', 'date_joined', 'role', 
            'is_Faculty', 'is_superuser', 'groups', 'department',
            'user_permissions', 'password', 'is_staff', 'is_UnitHead',
            'is_DepartmentHead', 'is_Admin', 'is_Faculty','faculty_rank', 'faculty_classification', 'faculty_tenure', 'faculty_status']

class UserUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    class Meta:

        model = User
        exclude = ['password']
        fields = ['first_name', 'last_name', 'email', 'alternative_email', 'faculty_rank', 'faculty_classification', 'faculty_tenure', 'faculty_status', 'password']