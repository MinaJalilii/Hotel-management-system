from django.contrib.auth import authenticate, login
from django.shortcuts import render
from userauths.models import User, Profile
from userauths.forms import UserCreationForm


def register_user_view(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            return "pass"
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            full_name = form.cleaned_data.get('full_name')
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            phone = form.cleaned_data.get('phone')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            user = authenticate(username=username, password=password1)
            if user is not None:
                login(request, user)
        context = {
            'form': form,
        }
        return render(request, 'userauths/register_user.html', context)
