from django.db import models

# Create your models here.
class Posts(models.Model):
    title_course = models.CharField(max_length=50)
    describe = models.TextField(default="no describe",null=True)
    day = models.DateField()
    time = models.TimeField()
