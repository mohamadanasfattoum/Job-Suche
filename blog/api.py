from rest_framework import generics
from .serializers import PostListSreializers, PostDetailSreializers
from .models import Post,Comments

class PostListApi(generics.ListCreateAPIView):
    serializer_class= PostListSreializers
    queryset= Post.objects.all()


class PostDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class= PostListSreializers
    queryset= Post.objects.all()