from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from taggit.managers import TaggableManager


class Post(models.Model):
    auther = models.ForeignKey(User, related_name='post_auther', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    post = models.TextField(max_length=50000)
    subtitle = models.TextField(max_length=1000)
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='post_image', null=True, blank=True)
    slug = models.SlugField(null=True,blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Post, self).save(*args, **kwargs)



class Comments(models.Model):
    auther = models.ForeignKey(User, related_name='comment_auther', on_delete=models.CASCADE)
    comment = models.TextField(max_length=5000)
    date = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, related_name='comment_post', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.post)