# from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment,Category
from django.shortcuts import redirect, get_object_or_404
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all().order_by('-date_posted')
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  
        content = request.POST.get('content')
        if content:
            Comment.objects.create(
                post=self.object,
                author=request.user,
                content=content
            )
        return redirect('post-detail', pk=self.object.pk)

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'image']  
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post-list')

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'image']  
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post-list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

class CategoryListView(ListView):
    model = Category
    template_name = 'blog/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(ListView):
    model = Post
    template_name = 'blog/category_detail.html'
    context_object_name = 'posts'

    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return self.category.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context