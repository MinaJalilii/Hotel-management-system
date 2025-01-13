from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from userauths.models import User, Profile
from userauths.forms import RegistrationForm
from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings


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


def login_user_view(request):
    # default_redirect_url = settings.LOGIN_REDIRECT_URL
    default_redirect_url = 'userauths:sign-up'

    if request.user.is_authenticated:
        return redirect(default_redirect_url)

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        next_url = request.POST.get('next')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)

            if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
                return redirect(next_url)
            else:
                return redirect(default_redirect_url)
        else:
            return render(request, 'userauths/sign-in.html', {
                'error': 'Invalid username or password',
                'next': next_url,
            })

    next_url = request.GET.get('next', 'userauths:sign-up')
    return render(request, 'userauths/sign-in.html', {'next': next_url})
