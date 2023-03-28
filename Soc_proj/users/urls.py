from django.urls import path
from django.contrib.auth.views import LoginView,PasswordResetView,PasswordChangeView,PasswordChangeDoneView
from .import views

app_name='users'

urlpatterns = [
    path('logout/',views.LogOut.as_view(),name='logout'),
    
    path('signup/',views.SignUp.as_view(),name='signup'),
    
    path('login/',LoginView.as_view(template_name='users/login.html'),name='login'),
    
    path('password_reset_form/',PasswordResetView.as_view(template_name='users/password_reset_form.html'),name='password_reset_form'),
    
    path('password_change/',PasswordChangeView.as_view(template_name='users/password_change.html'),name='password_change_form'),
    
    path('password_change/done/',PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),name='password_change_done'),
]
