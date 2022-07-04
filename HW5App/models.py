from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from embed_video.fields import EmbedVideoField


class Topic(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class AgeGroup(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    age = models.ForeignKey(AgeGroup, on_delete=models.CASCADE)
    tutorial_Video = EmbedVideoField()
    videodescription = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title


class Quiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    question1 = models.CharField(max_length=50)
    question2 = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    points = models.IntegerField(null=False)

