from django.contrib import admin
from django.db.models.expressions import F
from .models import Post,Comment
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
