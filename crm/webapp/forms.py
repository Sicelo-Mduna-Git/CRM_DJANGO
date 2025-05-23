from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm 
from django.forms.widgets import TextInput, PasswordInput

# - Register / Create a user

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
      
        
# - Login a user

class LoginForm(AuthenticationForm):
  username = forms.CharField(widget = TextInput())
  password = forms.CharField(widget = PasswordInput())
  