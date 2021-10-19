from django.urls import path
from . import views

app_name = 'home'


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginbase, name = "loginbase"),
    path('logout/', views.logout_request, name = "logout_request"),
    path('signup/', views.signup, name = "signup"),
    path('personal_profile/', views.personal_profile, name = "personal_profile"),
    path('new_blog/', views.new_blog, name = "new_blog"),
    path('open_blog/', views.open_blog, name = "open_blog"),
]