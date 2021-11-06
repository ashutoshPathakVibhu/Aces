from django import forms
from .models import Post,Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title', 'image', 'content','tags']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'content',}