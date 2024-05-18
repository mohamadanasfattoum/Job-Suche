from rest_framework import generics
from .serializers import PostListSerializers ,PostDetailSerializers
from .models import Post,Comments

class PostListApi(generics.ListCreateAPIView):
    serializer_class= PostListSerializers
    queryset= Post.objects.all()


class PostDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class= PostDetailSerializers
    queryset= Post.objects.all()



