from django.urls import path
from . import views

app_name = 'home'


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginbase, name = "loginbase"),
    path('logout/', views.logout_request, name = "logout_request"),
    path('signup/', views.signup, name = "signup"),
    path('userProfile/', views.userProfile, name = "userProfile"),
    path('createBlog/', views.createBlog, name = "createBlog"),
    path('open_blog/', views.open_blog, name = "open_blog"),
]