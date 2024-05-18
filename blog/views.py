from django.shortcuts import render
from django.views import generic
from .models import Post, Comments



class PostList(generic.ListView):
    model=Post


class PostDetail(generic.DetailView):
    model=Post

class PostDetail(generic.CreateView):
    model=Post


class PostDetail(generic.DeleteView):
    model=Post


class PostDetail(generic.UpdateView):
    model=Post