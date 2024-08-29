from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'image_name', 'date', 'slug', 'content', 'author', 'tags']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user_name', 'user_email', 'text', 'post']