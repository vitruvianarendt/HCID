from django.db import models

# Create your models here.


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

    def __str__(self):
        return self.title
