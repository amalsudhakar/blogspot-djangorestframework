from rest_framework import serializers
from .models import BlogPost
from account.serializers import CustomUserSerializer

class BlogPostSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer()

    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'author']