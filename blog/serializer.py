from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','author','title','text']

class CommentSerializer(serializers.ModelSerializer):
    post_name = serializers.RelatedField(source='post', read_only=True)
    class Meta:
        model = Comment
        fields = ['id','post_name','author','text']
