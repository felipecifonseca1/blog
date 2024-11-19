# from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'image']  
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post-list')

    # def get_form(self, *args, **kwargs):
    
    #     form = super().get_form(*args, **kwargs)
    #     form.enctype = 'multipart/form-data'
    #     return form

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'image']  
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post-list')

    # def get_form(self, *args, **kwargs):
    #     form = super().get_form(*args, **kwargs)
    #     form.enctype = 'multipart/form-data'
    #     return form

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')