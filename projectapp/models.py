from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    tech = models.CharField(max_length=20)
    img = models.FilePathField(path="/img")
