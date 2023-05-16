from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=255, null=True)
    slug = models.SlugField(unique=True)
    dese = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)