from datetime import timezone
from django.shortcuts import redirect, render
from django.views.generic.dates import timezone_today
from blog_app.models import Post, Comments
from blog_app.forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic import (TemplateView,
                                 ListView,
                                 DetailView,
                                 CreateView,
                                 UpdateView,
                                 DeleteView,
                                 )
# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    

class PostDetailView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin, CreateView):
    # This line help us to do not allow others to create posts
    login_url = '/login/'
    redirect_field_name = 'blog_app/post_detail.html'
    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/post_detail.html'
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login'
    redirect_field_name = 'blog_app/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__insull=True).order_by('created_date')