from django.db import models
from django.template.defaultfilters import slugify #For Adding Slugs of post's url
from django.contrib.auth.models import User  #For Authentication of Users
# Create your models here.

# Database Fields
class Post (models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.TextField()


# Permlink; unique url
@models.permalink
def get_absolute_url(self):
    return ('blog_post_detail', (),
            {
                'slug': self.slug,
            })


def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


# This will tell the web app how to arrange these posts in order; and not randomly. Logic in in this class
class Meta:
    ordering = ['created_on']

    def __unicode__(self):
        return self.title


# Comment table in the database
class Comment(models.Model):
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)