from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse, reverse_lazy
from posts.models import Post
from comments.models import Comment
from comments.forms import CommentForm


class PostList(ListView):
    """Список объектов модели Post"""
    model = Post
    template_name = 'post_list.html'


    def get_queryset(self):
        return Post.objects.order_by('-date_pub')


class PostDetail(DetailView):
    """
    один объект Post,
    и список комментариев с вложенностью
    и пагинацией
    """
    model = Post
    template_name = 'post_detail.html'
    success_url = reverse_lazy('posts:list')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment_form = CommentForm(user=self.request.user,
                                    post_id=None)
        context['post'] = self.get_object
        context['comment_form'] = comment_form 
        return context
