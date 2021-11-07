from django.db import models
from users.models import Profile
from django.utils.text import slugify 
import string
import random
from django.contrib.auth.models import User

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
    tags = models.CharField(null=True,max_length=200)
    image = models.ImageField(upload_to='blog_pics',blank=True)
    content = models.TextField()
    date = models.DateField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.title + ' by ' + self.author.first_name

    def save(self , *args, **kwargs): 
        self.slug = generate_slug(self.title)
        super(Post, self).save(*args, **kwargs)
    
    def get_tags_list(self):
        data = self.tags
        tags = [x.strip() for x in data.split(',')]
        return tags;

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField(max_length=160)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.post.title,str(self.user.first_name))


# UpVotes
class UpVote(models.Model):
    comment=models.ForeignKey(Comment,on_delete=models.CASCADE)
    user=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='upvote_user')

# DownVotes
class DownVote(models.Model):
    comment=models.ForeignKey(Comment,on_delete=models.CASCADE)
    user=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='downvote_user')