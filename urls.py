from django.contrib import admin
from django.urls import path 
from .import views
from django.contrib.auth import views as auth_views
from .views import test_email
from django.contrib.auth.views import (
    PasswordResetCompleteView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
)

app_name ='user'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('register/',views.register, name='register'),
    path('login/',views.user_login,name='login'),  
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout, name='logout'),
    path('change-password/', views.change_password, name='change_password'),
    path('test-email/', test_email, name='test-email'),


    path('password_reset/', PasswordResetView.as_view(
        template_name='user/password_reset.html',
        email_template_name='user/password_reset_email.html'
    ), name='password_reset'), 

    path('password_reset_done/', PasswordResetDoneView.as_view(
        template_name='user/password_reset_done.html'), name='password_reset_done'),
    
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='user/password_reset_confirm.html'
    ), name='password_reset_confirm'),

    path('password_reset_complete/', PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name='password_reset_complete'),
    
    path('password-reset_email/',PasswordResetView.as_view(
        template_name='users/password_reset.html',html_email_template_name='users/password_reset_email.html'),
    name='password-reset'),
]


