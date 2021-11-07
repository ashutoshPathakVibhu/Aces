from django.contrib import admin
from django.db.models.expressions import F
from .models import Post,Comment,UpVote,DownVote
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UpVote)
admin.site.register(DownVote)
