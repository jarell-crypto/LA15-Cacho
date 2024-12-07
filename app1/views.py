from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def say_hello(request):
    return HttpResponse('Hello Django')

def say_hi(request):
    return render(request, 'hi.html', {'name': 'Jarell'})

def blog_list(request):
    post = Post.objects.all()
    context = {
        'blog_list': post
    }
    return render(request, 'blog_list.html', context)

def blog_detail(request, id):
    each_post = Post.objects.get(id = id)
    context = {
        'blog_detail': each_post
    }
    return render(request, 'blog_detail.html', context)

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})