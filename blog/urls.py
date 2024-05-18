from django.urls import path
from .views import PostList, PostDetail
from .api import PostListApi, PostDetailApi




urlpatterns = [
    path('', PostList.as_view()),
    path('<slug:slug>', PostDetail.as_view()),


    path('postlistapi/', PostListApi.as_view()),
    path('postlistapi/<int:pk>', PostDetailApi.as_view()),


]
