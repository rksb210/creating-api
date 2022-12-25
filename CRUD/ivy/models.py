from django.db import models
from datetime import datetime


class Task(models.Model):
    photo = models.ImageField(upload_to="myimages")
    date = models.DateTimeField(auto_created=True)
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    status = models.CharField(max_length=100)



    
# Create your models here.
