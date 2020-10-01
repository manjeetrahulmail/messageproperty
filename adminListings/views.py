from django.shortcuts import render, redirect, get_object_or_404

from .models import AdminListing
from django.core.paginator import Paginator
import re

from accounts.models import Account

# Create your views here.
def adminListings(request):
    listings = AdminListing.objects.order_by('-listDate').filter(propertyStatus='Available')

    # connectionTypeFiltered = []
    # locationFiltered = []
    # offerTypeFiltered = []
    # propertyTypeFiltered = []

    # finalList = []

    # if request.method == 'POST':

    #     main_direct = ''
    #     owner = ''
    #     mptp = ''
    #     broker = ''
    #     coliving = ''
    #     serviceApartment = ''
    #     locality = ''
    #     rent = ''
    #     resale = ''
    #     newSale = ''
    #     one = ''
    #     two = ''
    #     three = ''
    #     four = ''
    #     five = ''
    #     price = 0

    #     if 'main_direct' in request.POST:
    #         main_direct = request.POST['main_direct']

    #     if 'owner' in request.POST:
    #         owner = request.POST['owner']

    #     if 'mptp' in request.POST:
    #         mptp = request.POST['mptp']

    #     if 'broker' in request.POST:
    #         broker = request.POST['broker']

    #     if 'coliving' in request.POST:
    #         coliving = request.POST['coliving']

    #     if 'serviceApartment' in request.POST:
    #         serviceApartment = request.POST['serviceApartment']

    #     if 'locality' in request.POST:
    #         locality = request.POST['locality']

    #     if 'rent' in request.POST:
    #         rent = request.POST['rent']

    #     if 'resale' in request.POST:
    #         resale = request.POST['resale']

    #     if 'newSale' in request.POST:
    #         newSale = request.POST['newSale']

    #     if 'one' in request.POST:
    #         one = request.POST['one']

    #     if 'two' in request.POST:
    #         two = request.POST['two']

    #     if 'three' in request.POST:
    #         three = request.POST['three']

    #     if 'four' in request.POST:
    #         four = request.POST['four']

    #     if 'five' in request.POST:
    #         five = request.POST['five']

    #     if 'price' in request.POST and request.POST['price']:
    #         price = int(request.POST['price'])

    #     if not (main_direct == 'on' or owner == 'on' or mptp == 'on' or broker == 'on' or coliving == 'on' or serviceApartment == 'on' or locality or rent == 'on' or resale == 'on' or newSale == 'on' or one == 'on' or two == 'on' or three == 'on' or four == 'on' or five == 'on' or price != 0):
    #         return redirect(request.META.get('HTTP_REFERER', '/'))

    #     if listings:
    #         if main_direct == 'on' or owner == 'on' or mptp == 'on' or broker == 'on' or coliving == 'on' or serviceApartment == 'on':
    #             for listing in listings:
    #                 if main_direct == 'on' and listing.connectionType == 'Main/Direct':
    #                     connectionTypeFiltered.append(listing)
    #                 if owner == 'on' and listing.connectionType == 'Owner':
    #                     connectionTypeFiltered.append(listing)
    #                 elif mptp == 'on' and listing.connectionType == 'Starred Owner':
    #                     connectionTypeFiltered.append(listing)
    #                 elif broker == 'on' and listing.connectionType == 'Broker':
    #                     connectionTypeFiltered.append(listing)
    #                 elif coliving == 'on' and listing.connectionType == 'Coliving':
    #                     connectionTypeFiltered.append(listing)
    #                 elif serviceApartment == 'on' and listing.connectionType == 'Service Apartment':
    #                     connectionTypeFiltered.append(listing)
    #         else:
    #             connectionTypeFiltered = listings

    #         if connectionTypeFiltered:
    #             if locality:
    #                 for listing in connectionTypeFiltered:
    #                     if re.search(locality, listing.locality, re.IGNORECASE):
    #                         locationFiltered.append(listing)
    #             else:
    #                 locationFiltered = connectionTypeFiltered

    #             if locationFiltered:
    #                 if rent == 'on' or resale == 'on' or newSale == 'on':
    #                     for listing in locationFiltered:
    #                         if rent == 'on' and listing.offerType == 'Rent':
    #                             offerTypeFiltered.append(listing)
    #                         elif resale == 'on' and listing.offerType == 'Resale':
    #                             offerTypeFiltered.append(listing)
    #                         elif newSale == 'on' and listing.offerType == 'New Sale':
    #                             offerTypeFiltered.append(listing)
    #                 else:
    #                     offerTypeFiltered = locationFiltered

    #                 if offerTypeFiltered:
    #                     if one == 'on' or two == 'on' or three == 'on' or four == 'on' or five == 'on':
    #                         for listing in offerTypeFiltered:
    #                             if one == 'on' and listing.one_bhk == True:
    #                                 propertyTypeFiltered.append(listing)
    #                             elif two == 'on' and listing.two_bhk == True:
    #                                 propertyTypeFiltered.append(listing)
    #                             elif three == 'on' and listing.three_bhk == True:
    #                                 propertyTypeFiltered.append(listing)
    #                             elif four == 'on' and listing.four_bhk ==True:
    #                                 propertyTypeFiltered.append(listing)
    #                             elif five == 'on' and listing.fivePlus_bhk == True:
    #                                 propertyTypeFiltered.append(listing)
    #                     else:
    #                         propertyTypeFiltered = offerTypeFiltered

    #                     if propertyTypeFiltered:
    #                         if price != 0:
    #                             for listing in propertyTypeFiltered:
    #                                 if price != 0 and listing.price <= price:
    #                                     finalList.append(listing)
    #                         else:
    #                             finalList = propertyTypeFiltered

    # else:
    #     finalList = listings
    
    # paginator = Paginator(finalList, 9) # Show 9 contacts per page.

    paginator = Paginator(listings, 9) # Show 9 contacts per page.
    page_number = request.GET.get('page')
    listings_obj = paginator.get_page(page_number)

    context = {
        'listings': listings_obj,
    }

    return render(request, 'listings/listings.html', context)

def filterAdminListings(request):

    listings = AdminListing.objects.order_by('-listDate').filter(propertyStatus='Available')

    connectionTypeFiltered = []
    locationFiltered = []
    offerTypeFiltered = []
    propertyTypeFiltered = []

    finalList = []

    main_direct = ''
    owner = ''
    mptp = ''
    broker = ''
    coliving = ''
    serviceApartment = ''
    locality = ''
    rent = ''
    resale = ''
    newSale = ''
    one = ''
    two = ''
    three = ''
    four = ''
    five = ''
    price = 0

    if 'main_direct' in request.GET:
        main_direct = request.GET['main_direct']

    if 'owner' in request.GET:
        owner = request.GET['owner']

    if 'mptp' in request.GET:
        mptp = request.GET['mptp']

    if 'broker' in request.GET:
        broker = request.GET['broker']

    if 'coliving' in request.GET:
        coliving = request.GET['coliving']

    if 'serviceApartment' in request.GET:
        serviceApartment = request.GET['serviceApartment']

    if 'locality' in request.GET:
        locality = request.GET['locality']

    if 'rent' in request.GET:
        rent = request.GET['rent']

    if 'resale' in request.GET:
        resale = request.GET['resale']

    if 'newSale' in request.GET:
        newSale = request.GET['newSale']

    if 'one' in request.GET:
        one = request.GET['one']

    if 'two' in request.GET:
        two = request.GET['two']

    if 'three' in request.GET:
        three = request.GET['three']

    if 'four' in request.GET:
        four = request.GET['four']

    if 'five' in request.GET:
        five = request.GET['five']

    if 'price' in request.GET and request.GET['price']:
        price = int(request.GET['price'])

    if not (main_direct == 'on' or owner == 'on' or mptp == 'on' or broker == 'on' or coliving == 'on' or serviceApartment == 'on' or locality or rent == 'on' or resale == 'on' or newSale == 'on' or one == 'on' or two == 'on' or three == 'on' or four == 'on' or five == 'on' or price != 0):
        return redirect(request.META.get('HTTP_REFERER', '/'))

    if listings:
        if main_direct == 'on' or owner == 'on' or mptp == 'on' or broker == 'on' or coliving == 'on' or serviceApartment == 'on':
            for listing in listings:
                if main_direct == 'on' and listing.connectionType == 'Main/Direct':
                    connectionTypeFiltered.append(listing)
                if owner == 'on' and listing.connectionType == 'Owner':
                    connectionTypeFiltered.append(listing)
                elif mptp == 'on' and listing.connectionType == 'Starred Owner':
                    connectionTypeFiltered.append(listing)
                elif broker == 'on' and listing.connectionType == 'Broker':
                    connectionTypeFiltered.append(listing)
                elif coliving == 'on' and listing.connectionType == 'Coliving':
                    connectionTypeFiltered.append(listing)
                elif serviceApartment == 'on' and listing.connectionType == 'Service Apartment':
                    connectionTypeFiltered.append(listing)
        else:
            connectionTypeFiltered = listings

        if connectionTypeFiltered:
            if locality:
                for listing in connectionTypeFiltered:
                    if re.search(locality, listing.locality, re.IGNORECASE):
                        locationFiltered.append(listing)
            else:
                locationFiltered = connectionTypeFiltered

            if locationFiltered:
                if rent == 'on' or resale == 'on' or newSale == 'on':
                    for listing in locationFiltered:
                        if rent == 'on' and listing.offerType == 'Rent':
                            offerTypeFiltered.append(listing)
                        elif resale == 'on' and listing.offerType == 'Resale':
                            offerTypeFiltered.append(listing)
                        elif newSale == 'on' and listing.offerType == 'New Sale':
                            offerTypeFiltered.append(listing)
                else:
                    offerTypeFiltered = locationFiltered

                if offerTypeFiltered:
                    if one == 'on' or two == 'on' or three == 'on' or four == 'on' or five == 'on':
                        for listing in offerTypeFiltered:
                            if one == 'on' and listing.one_bhk == True:
                                propertyTypeFiltered.append(listing)
                            elif two == 'on' and listing.two_bhk == True:
                                propertyTypeFiltered.append(listing)
                            elif three == 'on' and listing.three_bhk == True:
                                propertyTypeFiltered.append(listing)
                            elif four == 'on' and listing.four_bhk ==True:
                                propertyTypeFiltered.append(listing)
                            elif five == 'on' and listing.fivePlus_bhk == True:
                                propertyTypeFiltered.append(listing)
                    else:
                        propertyTypeFiltered = offerTypeFiltered

                    if propertyTypeFiltered:
                        if price != 0:
                            for listing in propertyTypeFiltered:
                                if price != 0 and listing.price <= price:
                                    finalList.append(listing)
                        else:
                            finalList = propertyTypeFiltered

    paginator = Paginator(finalList, 9) # Show 9 contacts per page.
    page_number = request.GET.get('page')
    listings_obj = paginator.get_page(page_number)

    context = {
        'listings': listings_obj,
    }

    return render(request, 'listings/listings.html', context)

def adminListing(request, listing_id):
    listing = get_object_or_404(AdminListing, pk=listing_id)

    if AdminListing.objects.filter(pk=listing_id).exists():
        if not(request.user.is_authenticated and request.user.whatsapp == listing.whatsapp):
            users = Account.objects.filter(whatsapp=listing.whatsapp)
            if users:
                users[0].clicks += 1
                users[0].save()

    context = {
        'listing': listing,
    }

    return render(request, 'listings/listing.html', context)