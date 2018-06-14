from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250, default ='')
    post = models.CharField(max_length=500)
    location = models.CharField(max_length=100, default ='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    salary = models.IntegerField(default=0)
    slug = models.SlugField(max_length=250,unique=True,)

    def save(self, *args, **kwargs):
        if not self.slug:
         self.slug = slugify(self.post)  # set the slug explicitly
         super(Post, self).save(*args, **kwargs)  # call Django's save()

    def __str__(self):
        return self.title


class Apply(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    add_on = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('home:home', kwargs={'pk':self.id})