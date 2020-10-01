from django.urls import path
from . import views

urlpatterns = [
    path('', views.sendContent, name='sendContent'),
    path('sendtenantemails', views.send_tenant_emails, name='send_tenant_emails'),
    path('sendowneremails', views.send_owner_emails, name='send_owner_emails'),
]