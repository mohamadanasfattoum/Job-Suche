from django.urls import path
from .views import PostList, PostDetail, CreatePost, UpdatePost, DeletePost
from .api import PostListApi, PostDetailApi




urlpatterns = [
    path('', PostList.as_view()),
    path('<slug:slug>', PostDetail.as_view()),
    path('add/', CreatePost.as_view()),
    path('delete/<int:pk>', DeletePost.as_view()),
    path('update/<int:pk>', UpdatePost.as_view()),


    path('postlistapi/', PostListApi.as_view()),
    path('postlistapi/<int:pk>', PostDetailApi.as_view()),


]
