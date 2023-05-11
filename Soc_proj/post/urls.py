from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    
    path('', views.index, name = 'General'),
    
    path('group/<slug:slugs>/', views.group_posts, name = 'Groups'),
    
    path('profile/<str:username>/',views.profile,name='profile'),
    
    path('posts/<int:post_id>/',views.post_detail,name='post_detail'),
    
    path('posts/<int:post_id>/comment', views.add_comment, name='add_comment'),
    
    path('create/',views.post_create,name='post_create'),

]