from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),

    path('reset-password', auth_views.PasswordResetView.as_view(template_name='accounts/resetPassword.html'), name='reset_password'),

    path('reset-password-sent', auth_views.PasswordResetDoneView.as_view(template_name='accounts/resetPasswordSent.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/resetPasswordConfirm.html'), name='password_reset_confirm'),

    path('reset-password-complete', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/resetPasswordComplete.html'), name='password_reset_complete'),

]