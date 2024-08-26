from django.db import models

# Create your models here.
class Posts(models.Model):
    title_course = models.CharField(max_length=50)
    describe = models.TextField(default="no describe", null=True)
    day = models.DateField(auto_now_add=True)  # Automatically set the date when the object is created
    time = models.TimeField(auto_now_add=True)  # Automatically set the time when the object is created
    images = models.ImageField(upload_to="images", null=True)
