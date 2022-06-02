from django.shortcuts import render
from .models import BlogPost


# Create your views here.
def index(request):
    posts = BlogPost.objects.all()
    return render(request, "blog/index.html", {'posts': posts})


def blogpost(request, id):
    post = BlogPost.objects.filter(id=id)[0]
    posts = BlogPost.objects.all()
    n = len(posts)
    return render(request, 'blog/blogpost.html', {'post': post, 'n': n + 1})
