from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import Blog
from django import forms
class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","first_name","email"]
class LoginForm(AuthenticationForm):
    pass

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=["title","description"]