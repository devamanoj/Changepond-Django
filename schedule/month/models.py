from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator 

# Create your models here.
class author(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    age=models.IntegerField(validators=[MinValueValidator(18) , MaxValueValidator(59)])
    city = models.CharField(max_length=100,null=True)
    rating = models.IntegerField(validators=[
        MaxValueValidator(5),MinValueValidator(2)
    ],null=True)

    def __str__(self) -> str:   
        return f'{self.first_name} and {self.last_name}'
