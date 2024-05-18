from django.shortcuts import render
from django.views import generic
from .models import Post, Comments



class PostList(generic.ListView):
    model=Post


class PostDetail(generic.DetailView):
    model = Post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comment = post.comment_post.all()
        context['comments'] = comment
        return context



# class PostDetail(generic.CreateView):
#     model=Post


# class PostDetail(generic.DeleteView):
#     model=Post


# class PostDetail(generic.UpdateView):
#     model=Post