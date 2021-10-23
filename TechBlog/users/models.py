from django.db import models
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone

# Create your models here.

def get_path(instance, filename):
    extension = filename.split('.')[-1]
    uuid_name = uuid.uuid1().hex
    return f'profile_image/{uuid_name}.{extension}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(blank=False, max_length=256, unique=False)
    last_name = models.CharField(blank=True, max_length=256, unique=False)
    image = models.ImageField(upload_to=get_path,blank=True)

    def __str__(self):
        return f'{self.user.username}-{self.user.pk}'

    # def save(self, *args, **kwargs):
    #     super(Profile, self).save(*args, **kwargs)

def create_profile(self, **kwargs):
    Profile.objects.create(
        user=self,
        **kwargs # you can pass other fields values upon creating
    )
User.add_to_class('create_profile', create_profile)
