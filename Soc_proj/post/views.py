from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Post,Group


def index(request):
    template = 'post/index.html'
    
    posts = Post.objects.order_by('-pub_date')[:10]
    title = 'Главная страница'
    text = 'Это главная страница проекта'
    
    context = {'title':title, 'text':text, 'posts':posts}
    
    return render(request, template, context)


def group_posts(request, slugs):
    template = 'post/group_post.html'
    group = get_object_or_404(Group,adress=slugs)
    posts=Post.objects.filter(group=group).order_by('-pub_date')[:10]
    title = 'Группы'

    context = {'title':title, 'group':group, 'posts':posts}
    
    return render(request, template, context)



