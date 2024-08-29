from django.db import models

# Create your models here.
# class Author(models.Model):
#     name = models.CharField(max_length=30)
#     city = models.CharField(max_length=30)
#     age  = models.IntegerField()
#     image = models.ImageField(upload_to=author_image_file_path,null=True,blank=True)

class Category(models.Model):
    name = models.CharField(max_length=30)
    
class Dish(models.Model):
    dishname = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes')