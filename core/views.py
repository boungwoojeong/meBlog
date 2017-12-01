
from django.shortcuts import render, HttpResponse
from core.models import Post
def hello_world(request):

    return HttpResponse("Hello World")


def index(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'index.html', dict(posts=posts))

def article_detail(reqeust, pk):
    post = Post.objects.get(pk=pk)
    return render(reqeust, 'article_detail.html', dict(post=post))
