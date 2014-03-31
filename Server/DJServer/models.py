from django.db import models


# Create your models here.



class File(models.Model):
    id = models.AutoField(primary_key=True)
    fileName = models.CharField(max_length=500)

    fileHash = models.CharField(max_length=256)
    timestamp = models.TimeField()

