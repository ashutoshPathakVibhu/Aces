from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import Post
# Create your views here.

def index(request):
    context = {}
    blogs_all = Post.objects.all()
    context['blogs'] = blogs_all
    return render(request,"userProfile.html",context)

def blog_detail(request,slug):
    context = {}
    blog = Post.objects.get(slug=slug)
    context['blog'] = blog
    return render(request,"blog_details.html",context)

def create_blog(request):
    context = {}
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES)
        form.instance.author=request.user.profile
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
        context['form'] = form
        return render(request,'createBlog.html',context)
    form = BlogForm()
    return render(request,'createBlog.html',context)

def tag_view(request,tag):
    posts = Post.objects.all()
    context = {}
    context['blogs'] = []
    for post in posts:
        tag_list = post.get_tags_list()
        print(tag_list)
        if tag in tag_list:
                context['blogs'].append(post)
    return render(request,"userProfile.html",context)