from django.contrib import admin
from django.db.models.expressions import F
from .models import Post
# Register your models here.
admin.site.register(Post)