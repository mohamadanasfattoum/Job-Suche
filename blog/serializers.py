from rest_framework import serializers
from .models import Post,Comments



class CommentsSerializers(serializers.ModelSerializer):
    post = serializers.StringRelatedField()
    class Meta:
        model = Comments
        fields = '__all__'



class PostListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostDetailSerializers(serializers.ModelSerializer):

    comments =CommentsSerializers(many=True, source = 'comment_post')
    class Meta:
        model = Post
        fields = '__all__'



