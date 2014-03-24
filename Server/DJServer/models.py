from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    passHash = models.CharField(max_length=256)

class File(models.Model):
    id = models.AutoField(primary_key=True)
    fileName = models.CharField(max_length=500)
    name = models.ForeignKey(User)
    fileHash = models.CharField(max_length=256)
    timestamp = models.TimeField()

