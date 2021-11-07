from django.shortcuts import render, redirect
from .forms import *
from .models import Post, Comment, UpVote, DownVote
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from users.models import Profile
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
    return render(request, 'createBlog.html', context)


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
