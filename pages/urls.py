from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:whatsapp>', views.listing, name='listing'),  #No negative urls
    path('about', views.about, name='about'),
    path('how-it-works', views.howItWorks, name='howItWorks'),
    path('loaderio-003734d6f270f6f6a577843a18e13526.txt', views.loaderIO2, name='loaderIO2'),
    path('comingsoon', views.comingSoon, name='comingSoon'),
]