from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/html/all_blogs.html', {'blogs': blogs, 'title': 'All blogs'})


def detail(request, blog_id):
    # blog = Blog.objects.all()[blog_id - 1]
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/html/detail.html', {'blog': blog, 'title': f'{blog.title}'})