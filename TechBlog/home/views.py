from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def index(request):
    return render(request, 'index.html')

def loginbase(request):
    return render(request,'login.html')

def logout_request(request):
    return HttpResponse('<h1>logout page here </h1>')

def signup(request):
    return render(request,'register.html')

def userProfile(request):
    return render(request,'userProfile.html')

def createBlog(request):
    return render(request,'createBlog.html')

def open_blog(request):
    return render(request,'open_blog.html')
