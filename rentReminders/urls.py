from django.urls import path
from . import views

urlpatterns = [
    path('', views.tenantForm, name='tenantForm'),
]