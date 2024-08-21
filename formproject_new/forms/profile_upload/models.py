from django.db import models

# Create your models here.
class profile(models.Model):
    image = models.FileField(upload_to='')
class profile1(models.Model):
    image = models.FileField(upload_to='')