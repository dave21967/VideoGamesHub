import datetime
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    news_letter = models.BooleanField(default=True)
    bio = models.TextField(default="")
    level = models.IntegerField(default=1)
    total_xp = models.IntegerField(default=0)
    missing_xp = models.IntegerField(default=200)
    profile_pic = models.ImageField(upload_to="profile_pics", blank=True)

class Post(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    slug = models.SlugField(blank=False)
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField()
    cover = models.ImageField(upload_to="post_covers")
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    tags = models.CharField(max_length=50, blank=False)
    views = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)