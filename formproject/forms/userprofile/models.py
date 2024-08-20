from django.db import models

# Create your models here.
class review(models.Model):
    user_name = models.CharField(max_length=30)
    rating = models.IntegerField()
    massage = models.TextField()
    