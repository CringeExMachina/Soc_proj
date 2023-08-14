from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter

router=SimpleRouter()
router.register('post', views.PostViewSet)

app_name = 'post'

urlpatterns = [
    
    path('', views.index, name = 'General'),
    
    path('group/<slug:slugs>/', views.group_posts, name = 'Groups'),
    
    path('profile/<str:username>/',views.profile,name='profile'),
    
    path('posts/<int:post_id>/comment', views.add_comment, name='add_comment'),
    
    path('posts/<int:post_id>/',views.post_detail,name='post_detail'),
    
    path('create/',views.post_create,name='post_create'),
    
    path('api/v1/posts', include(router.urls))
    


]