from django.contrib import admin
# импорт include позволит использовать адреса, включенные в приложения
from django.urls import include, path

urlpatterns = [
    # Сначала проверяем все пути, которые есть в приложении ice_cream
    path('', include('post.urls', namespace='post')),
    path('admin/', admin.site.urls),
    ]