from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/index.html', {'posts': posts})
def content(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/content.html', {'post': post})
def cv(request):
    return render(request, 'blog/cv.html', {})
def about(request):
    return render(request, 'blog/about.html', {})
