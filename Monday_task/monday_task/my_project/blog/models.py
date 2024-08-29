from django.db import models

class TagLine(models.Model):
    caption = models.CharField(max_length=255)

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.EmailField(unique=True)

class Post(models.Model):
    title = models.CharField(max_length=255)
    image_name = models.CharField(max_length=255)
    date = models.DateField()
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(TagLine)

class Comment(models.Model):
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField()
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)