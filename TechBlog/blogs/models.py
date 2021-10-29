from django.db import models
from users.models import Profile
from django.utils.text import slugify 
import string
import random
# Create your models here.

def generate_random_string(N): 
    res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = N))
    return res
  
def generate_slug(text):
    new_slug = slugify(text)
    if Post.objects.filter(slug = new_slug).first():
        return generate_slug(text + generate_random_string(5))
    return new_slug

class Post(models.Model):
    author = models.ForeignKey(Profile , on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100,null=True,blank=True)
    title = models.CharField(blank=False,unique=False,max_length=50)
    image = models.ImageField(upload_to='blog_pics',blank=True)
    content = models.TextField()
    date = models.DateField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.title + ' by ' + self.author.first_name

    def save(self , *args, **kwargs): 
        self.slug = generate_slug(self.title)
        super(Post, self).save(*args, **kwargs)