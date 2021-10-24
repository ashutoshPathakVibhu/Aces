from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request, "Successfully Logged In")
            return redirect('/')
        else:
            messages.error(request,'Invalid Credentials, Please try again')
            return render(request,'login.html')

    else:
        messages.error(request,'GETTTTTTTTTTT')
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def signup(request):
    return render(request,'register.html')

def userProfile(request):
    return render(request,'userProfile.html')

def createBlog(request):
    return render(request,'createBlog.html')

def open_blog(request):
    return render(request,'open_blog.html')
