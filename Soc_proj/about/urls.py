from django.urls import path
from . import views
app_name='about'

urlpatterns = [
    path('author/',views.AboutPage.as_view(),name='author')
]

