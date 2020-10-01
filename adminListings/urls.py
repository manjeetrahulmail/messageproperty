from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminListings, name='adminListings'),
    path('<int:listing_id>', views.adminListing, name='adminListing'),
    path('filter-main', views.filterAdminListings, name='filterAdminListings'),
]