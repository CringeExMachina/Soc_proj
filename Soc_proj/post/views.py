from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'post/index.html'
    return render(request, template)


def group_posts(request, slugs):
    template = 'post/group_post.html'
    return render(request, template)



