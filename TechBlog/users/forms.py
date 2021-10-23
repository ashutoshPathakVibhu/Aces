from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=256)
    last_name = forms.CharField(max_length=256)
    image = forms.ImageField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'image', 'first_name', 'last_name']
    
    def save(self,commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']

        user.save()
        user.create_profile() 

        # user has to be saved to add profile
        user.profile.first_name = self.cleaned_data['first_name']
        user.profile.last_name = self.cleaned_data['last_name']
        user.profile.image = self.cleaned_data.get('image')
        user.profile.save()

        if commit:
            user.save()