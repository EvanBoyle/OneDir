from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    passHash = models.CharField(max_lengh=256)
    
