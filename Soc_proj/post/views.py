from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная')


def group_posts(request, slugs):
    return HttpResponse(f'Список постов {slugs}')



