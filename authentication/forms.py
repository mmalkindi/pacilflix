from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms
from django_countries.fields import CountryField

class PenggunaCreationForm(UserCreationForm):
    country = CountryField().formfield()

    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'username'}) 
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'newpassword'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'pw2'})  
        self.fields['country'].widget.attrs.update({'class': 'form-control'}) 