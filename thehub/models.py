import datetime
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User

class GameCathegory(models.Model):
    title = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.title

class DevRequest(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

class Game(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    title = models.CharField(max_length=50)
    cover = models.ImageField(upload_to="games_covers")
    description = models.TextField()
    files = models.FileField(upload_to="game_files", default="")
    pegi = models.IntegerField(default=3)
    pub_date = models.DateTimeField(default=datetime.datetime.now())
    downloads = models.IntegerField(default=0)
    cathergory = models.ForeignKey(GameCathegory, on_delete=models.CASCADE)
    developer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class GameSave(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    data = models.JSONField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class Achievement(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    difficulty = models.IntegerField(default=0)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class GainAchievement(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)