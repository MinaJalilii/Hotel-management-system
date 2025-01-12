from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from userauths.models import User, Profile
from userauths.forms import RegistrationForm


def register_user_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            full_name = form.cleaned_data.get('full_name')
            phone = form.cleaned_data.get('phone')

            profile = Profile.objects.get(user=user)
            profile.full_name = full_name
            profile.phone = phone
            profile.save()

            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('userauths:sign-up')
    else:
        form = RegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'userauths/sign-up.html', context)
