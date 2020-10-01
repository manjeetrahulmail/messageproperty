from django.urls import path
from . import views

urlpatterns = [
    path('owner', views.ownerForm, name='ownerForm'),
    path('property-brands', views.propertyBrandsForm, name='propertyBrandsForm'),
    path('report', views.report, name='report'),
    path('edit-listing', views.editListing, name='editListing'),
    path('requirements', views.requirements, name='requirements'),

    path('edit-owner-property', views.editOwnerListing, name='editOwnerListing'),
    path('edit-property-brands-listing', views.editPropertyBrandsListing, name='editPropertyBrandsListing'),
    path('edit-main-<int:listing_id>', views.editAdminListing, name='editAdminListing'),
]