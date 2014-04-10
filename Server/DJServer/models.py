from django.db import models
from django.contrib.auth.models import User



# Create your models here.



class ODFile(models.Model):
    id = models.AutoField(primary_key=True)
    fileName = models.CharField(max_length=500)
    name = models.ForeignKey(User) #This is actually user ID. Username cannot be used, because calling User.get_username() requires making an instance of User
    fileHash = models.CharField(max_length=256)
    fileSize = models.IntegerField()
    timestamp = models.DateTimeField( auto_now_add=True)