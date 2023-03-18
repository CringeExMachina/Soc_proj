from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'post/index.html'
    
    title = 'Главная страница'
    text = 'Это главная страница проекта'
    context = {'title':title, 'text':text}
    
    return render(request, template, context)


def group_posts(request, slugs):
    template = 'post/group_post.html'
    
    title = 'Группы'
    text = 'Здесь будет информация о группах проекта'
    context = {'title':title, 'text':text}
    
    return render(request, template, context)



