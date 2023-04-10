from django.contrib import admin
# импорт include позволит использовать адреса, включенные в приложения
from django.urls import include, path

urlpatterns = [
    # Сначала проверяем все пути, которые есть в приложении
    path('about/',include('about.urls',namespace='about')),
    path('admin/', admin.site.urls),
    path('auth/',include('users.urls',namespace='users')),
    path('auth/', include('django.contrib.auth.urls')), 
    path('', include('post.urls', namespace='post'))
    
    
    ]