
from dataclasses import fields
from importlib.metadata import files
from pyexpat import model

from unicodedata import name
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Books
class studentform(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
class Bookform(forms.ModelForm):
    class Meta:
        model=Books
        fields="__all__"
        ##add it as tuple string which all to display 
class regform(UserCreationForm):
    class Meta:
        model=User
        fields=('first_name','last_name','email','username','password1','password2')
    