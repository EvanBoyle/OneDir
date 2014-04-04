from django.db import models
from django.contrib.auth.models import User



# Create your models here.



class ODFile(models.Model):
    id = models.AutoField(primary_key=True)
    fileName = models.CharField(max_length=500)
    name = models.ForeignKey(User)
    fileHash = models.CharField(max_length=256)
    timestamp = models.TimeField(auto_now=True)

