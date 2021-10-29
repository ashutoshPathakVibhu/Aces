from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blogs'


urlpatterns = [
    path('', views.index, name='index'),
    path('details/<slug>', views.blog_detail, name = "blog_detail"),
    path('create', views.create_blog, name = "create_blog"),
]
