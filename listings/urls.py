from django.urls import path
from . import views

urlpatterns = [
    path('owners', views.ownerListings, name='ownerListings'),
    path('property-brands', views.propertyBrandListings, name='propertyBrandListings'),
    path('brokers', views.brokerListings, name='brokerListings'),
    path('message-property-team-picks', views.mptpListings, name='mptpListings'),

    path('', views.listings, name='listings'),
    path('filter-properties', views.filterListings, name='filterListings'),
]