from django.urls import path
from django.contrib.auth.views import LogoutView
from .import views

app_name='users'

urlpatterns = [
    path('logout/',views.LogOut.as_view(),name='logout'),
    
    path('signup/',views.SignUp.as_view(),name='signup')
]
