from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def index(request):
    return render(request, 'index.html')

def loginbase(request):
    return HttpResponse('<h1>Login page here </h1>')

def logout_request(request):
    return HttpResponse('<h1>logout page here </h1>')

def signup(request):
    return HttpResponse('<h1>signup page here </h1>')

def personal_profile(request):
    return HttpResponse('<h1>personal_profile page here </h1>')

def new_blog(request):
    return HttpResponse('<h1>new_blog page here </h1>')

def open_blog(request):
    return HttpResponse('<h1>open_blog page here </h1>')
