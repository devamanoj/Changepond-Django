from django.db import models
 
# Create your models here.
 
def author_image_file_path(instance,filename):
    return '/'.join([str(instance.name),filename])
class Author(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    age  = models.IntegerField()
    image = models.ImageField(upload_to=author_image_file_path,null=True,blank=True)