from django.db import models
from django.contrib.auth.models import User
from Post.models import Post


# Create your models here.
class Page(models.Model):
    name = models.CharField(unique=True, max_length=42)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
