from django.contrib import admin
# импорт include позволит использовать адреса, включенные в приложения
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Сначала проверяем все пути, которые есть в приложении
    path('about/',include('about.urls',namespace='about')),
    path('admin/', admin.site.urls),
    path('auth/',include('users.urls',namespace='users')),
    path('auth/', include('django.contrib.auth.urls')), 
    path('', include('post.urls', namespace='post'))
    ]

handler404 = 'core.views.page_not_found'

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )