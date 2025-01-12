from django import forms
from userauths.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'full name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'phone number'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'confirm password'}))

    class Meta:
        model = User
        fields = ('full_name', 'username', 'email', 'phone', 'password1', 'password2')
