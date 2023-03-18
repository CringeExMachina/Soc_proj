from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.index, name = 'General'),
    
    path('group/<slug:slugs>/', views.group_posts, name = 'Groups')

]