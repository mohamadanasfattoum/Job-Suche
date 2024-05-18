from rest_framework import serializers
from .models import Post,Comments

class PostListSreializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostDetailSreializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'




