from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from authsysproject.settings import EMAIL_HOST_USER
from .forms import UserRegisterForm


def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            subject = 'Welcome to team The code Work'
            message = f'Hi  thank you for registration.'
            email_from = EMAIL_HOST_USER
            recipient_list = [form.cleaned_data.get('email'), ]
            send_mail(subject, message, email_from, recipient_list)
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'users/profile.html')
