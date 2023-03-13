from django.urls import path
from . import views

urlpatterns = [
    #General
    path('', views.index),
    #Post group
    path('group/<str:pk>/', views.group_posts)

]