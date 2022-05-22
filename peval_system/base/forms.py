from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
import sys

# sys.path.append("/Laptop Files/eval_sys_128.2/Performance-Evaluation-System/peval_system/users")
# from models import UserManager, User 

class GenericLoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)