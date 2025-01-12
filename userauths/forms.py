from django import forms
from userauths.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    full_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'full name', 'class': 'form-control', 'type': 'text', 'name': 'full_name'}))
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'username', 'class': 'form-control', 'type': 'text', 'name': 'username'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'email', 'class': 'form-control', 'type': 'email', 'name': 'email'}))
    phone = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'phone number', 'class': 'form-control', 'type': 'text', 'name': 'phone'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'password', 'class': 'form-control', 'type': 'password', 'name': 'password1'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'confirm password', 'class': 'form-control', 'type': 'password',
                   'name': 'password2'}))

    class Meta:
        model = User
        fields = ('full_name', 'username', 'email', 'phone', 'password1', 'password2')
