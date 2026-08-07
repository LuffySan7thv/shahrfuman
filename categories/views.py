from django.shortcuts import render, get_object_or_404
from .models import Category
from posts.models import Post

def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug, is_active=True)
    posts = Post.objects.filter(category=category).order_by('-created_at')
    
    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'categories/posts.html', context)
