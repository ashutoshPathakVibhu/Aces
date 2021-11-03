from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.models import User,auth
from django.contrib import messages
from users.models import Profile

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
            return render(request,'index.html')
        else:
            messages.error(request,'Invalid Credentials, Please try again')
            return render(request,'login.html')

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def signup(request):
    return render(request,'register.html')

def userProfile(request):
    if request.user.is_authenticated:
        us = request.user
        profile = Profile.objects.get(user = us)
        first_name = profile.first_name
        last_name = profile.last_name
        pic = profile.image
        return render(request,'userProfile.html',{'first_name':first_name,'last_name':last_name,'image':pic})
    else:
        return render(request,'login.html')

def createBlog(request):
    return render(request,'createBlog.html')

def blogList(request):
    return render(request,'blogList.html')

def open_blog(request):
    return render(request,'open_blog.html')
