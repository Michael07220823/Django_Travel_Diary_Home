from django.shortcuts import render
from .models import Post
import time
# Create your views here.

def home(request):
    post_list = Post.objects.all()
    return render(request, 'home.html', {
        'post_list': post_list,
    })


def hello_world(request):
    return render(request, "hello_world.html", 
    # https://www.runoob.com/python3/python3-date-time.html
    {'current_time': str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post})