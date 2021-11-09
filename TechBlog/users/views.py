from django import forms
from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib import messages
# Create your views here.

def index(request):
    return redirect('home:userProfile')

def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                messages.info(request, 'Registration Successful!')
                return redirect('home:userProfile')
        else:
            form = UserRegisterForm()
        messages.info(request, 'Invalid Credentials, Please try again')
        return render(request, 'register.html', {'form': form})
    else:
        messages.info(request, 'Invalid Credentials, Please try again')
        return redirect('home:index')