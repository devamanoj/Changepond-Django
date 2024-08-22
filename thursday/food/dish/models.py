from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
class Chef_details(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    address = models.CharField(max_length=30)

class Dish(models.Model):
    dish_name = models.CharField(max_length=20)
    rating = models.IntegerField(validators=[
        MinValueValidator(1),MaxValueValidator(5)
    ])
    chef = models.ForeignKey(Chef_details,on_delete=models.CASCADE,null=True)


# Create your models here= 