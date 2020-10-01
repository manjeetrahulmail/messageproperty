from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>', views.sale, name='sale'),
]