from django.db import models

# Create your models here.
class Dish(models.Model):
    dish_name = models.CharField(max_length=50)
    price = models.IntegerField()

