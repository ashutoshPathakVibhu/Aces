from django.core.checks import messages
from django.shortcuts import render, redirect, HttpResponse
from .decorators import allow_shares
from .forms import *
from .models import Post, Comment, UpVote, DownVote, ShareKey
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.urls import resolve
from django.utils.crypto import get_random_string
from users.models import Profile
from django.contrib import messages
# Create your views here.


def index(request):
    context = {}
    blogs_all = Post.objects.all()
    context['blogs'] = blogs_all
    return render(request, "blogList.html", context)


def blog_detail(request, slug):
    context = {}
    blog = Post.objects.get(slug=slug)
    comments = Comment.objects.filter(post=blog).order_by('-id')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            comment = Comment.objects.create(
                post=blog, user=request.user, content=content)
            comment.save()
            return redirect(f"/blogs/details/{blog.slug}")
    else:
        comment_form = CommentForm()

    context['blog'] = blog
    context['comments'] = comments
    context['comment_form'] = comment_form
    return render(request, "blog_details.html", context)


def create_blog(request):
    context = {}
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        form.instance.author = request.user.profile
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
        context['form'] = form
        return render(request, 'createBlog.html', context)
    form = BlogForm()
    context['form'] = form
    return render(request, 'createBlog.html', context)

@allow_shares
def update_blog(request,pk,*args,**kwargs):
    context = {}
    blog = Post.objects.get(pk=pk)
    print(blog)
    if request.method == 'GET':
        context['form'] = BlogForm(instance=blog)
        return render(request,'createBlog.html',context)
    else:
        form = BlogForm(request.POST,request.FILES,instance=blog)
        if form.is_valid():
            form.save()
            return redirect("blogs:index")
        else:
            messages.error(request,"Invalid form")
        return render(request,"createBlog.html",{'form':form})


def tag_view(request, tag):
    posts = Post.objects.all()
    context = {}
    context['blogs'] = []
    for post in posts:
        tag_list = post.get_tags_list()
        print(tag_list)
        if tag in tag_list:
            context['blogs'].append(post)
    return render(request, "blogList.html", context)


# Save Upvote
def save_upvote(request):
    if request.method == 'POST':
        commentid = request.POST['commentid']
        comment = Comment.objects.get(pk=commentid)
        user = Profile.objects.get(user=request.user)
        check = UpVote.objects.filter(comment=comment, user=user).count()
        if check > 0:
            return JsonResponse({'bool': False})
        else:
            UpVote.objects.create(
                comment=comment,
                user=user
            )
            return JsonResponse({'bool': True})

# Save Downvote
def save_downvote(request):
    if request.method == 'POST':
        commentid = request.POST['commentid']
        comment = Comment.objects.get(pk=commentid)
        user = Profile.objects.get(user=request.user)
        check = DownVote.objects.filter(comment=comment, user=user).count()
        if check > 0:
            return JsonResponse({'bool': False})
        else:
            DownVote.objects.create(
                comment=comment,
                user=user
            )
            return JsonResponse({'bool': True})


def sharedPage(request, key):
    try:
        try:
            shareKey = ShareKey.objects.get(pk=key)
        except: raise SharifyError
        # if shareKey.expired: raise SharifyError
        func, args, kwargs = resolve(shareKey.location)
        kwargs["__shared"] = True
        kwargs['pid'] = shareKey.blog.pk
        return func(request, *args, **kwargs)
    except SharifyError:
        return HttpResponse("This is beyond science") # or add a more detailed error page. This either means that the key doesn’t exist or is expired

def createShare(request, pk):
    task = Post.objects.get(pk=pk)
    try:
        key = task.sharekey
        key.delete()
        key = ShareKey.objects.create(blog=task,pk=get_random_string(40),
                                      expiration_seconds=60*60*24, # 1 day
                                      location = task.get_absolute_url_detail(),
                                      )
    except:
        key = ShareKey.objects.create(blog=task, pk=get_random_string(40),
                                      expiration_seconds=60 * 60 * 24,  # 1 day
                                      location=task.get_absolute_url_detail(),
                                      )
    key.save()
    return JsonResponse({"key":key.pk})

class SharifyError(Exception):pass