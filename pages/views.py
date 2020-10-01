from django.shortcuts import render, get_object_or_404, redirect
from forms.models import OwnerModel, PropertyBrandsModel

from itertools import chain
from django.contrib import messages
from django.db.models import Q

from accounts.models import Account
from django.conf import settings
from django.core.mail import EmailMessage

from adminListings.models import AdminListing

# Create your views here.
def index(request):

    # ownerListings = OwnerModel.objects.order_by('-listDate').filter(propertyStatus='Available', connectionType='Owner')

    # propertyBrandListings = PropertyBrandsModel.objects.order_by('-listDate').filter(propertyStatus='Available')

    # brokerListings = PropertyBrandsModel.objects.order_by('-listDate').filter(propertyStatus='Available', connectionType='Broker')

    # mptpListings = OwnerModel.objects.order_by('-listDate').filter(propertyStatus='Available', connectionType='Starred Owner')

    properties = list(chain(OwnerModel.objects.order_by('-listDate').filter(propertyStatus='Available'), PropertyBrandsModel.objects.order_by('-listDate').filter(propertyStatus='Available')))

    adminListings = AdminListing.objects.order_by('-listDate').filter(propertyStatus='Available')

    context = {
        # 'ownerListings': ownerListings,
        # 'propertyBrandListings': propertyBrandListings,
        # 'brokerListings': brokerListings,
        # 'mptpListings': mptpListings,
        'properties': properties,
        'adminListings': adminListings
    }

    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

def listing(request, whatsapp):

    listing = None

    if OwnerModel.objects.filter(whatsapp=whatsapp).exists():
        listing = get_object_or_404(OwnerModel, whatsapp=whatsapp)

    elif PropertyBrandsModel.objects.filter(whatsapp=whatsapp):
        listing = get_object_or_404(PropertyBrandsModel, whatsapp=whatsapp)

    if request.method == 'POST':
        if listing:
            status = request.POST['status']
            if status == 'Available':
                listing.propertyStatus = 'Not Available'
            else:
                listing.propertyStatus = 'Available'

            listing.save()

            if request.POST['status'] == 'Not Available':
                msg = request.user.first_name + ' ' + request.user.last_name + ' ' + 'has changed their property status.\nConnection Type: ' + request.POST['cType'] + '\nWhatsapp Number: ' + str(whatsapp)

                email = EmailMessage(
                    'Property Status Changed by User',
                    msg,
                    settings.EMAIL_HOST_USER,
                    ['manjeetrahulmail@gmail.com']
                )
                email.fail_silently = True
                email.send()

            storage = messages.get_messages(request)
            storage.used = True

            myLink = 'https://www.messageproperty.com/' + str(whatsapp)
            messages.success(request, 'Your status has been changed')
            messages.success(request, '<strong>Go to your listing : </strong><a href="' + myLink + '"><u>Click Here</u></a>', extra_tags='safe')
            messages.success(request, '<strong>Go to dashboard : </strong><a href = "https://www.messageproperty.com/accounts/dashboard"><u>Click Here</u></a>', extra_tags='safe')
            return redirect('editOwnerListing')

    if not (request.user.is_authenticated and request.user.whatsapp == str(whatsapp)):
        users = Account.objects.filter(whatsapp=whatsapp)
        if users:
            users[0].clicks +=  1
            users[0].save()

    if listing:
        context = {
            'listing': listing,
        }
        return render(request, 'listings/listing.html', context)

    else:
        storage = messages.get_messages(request)
        storage.used = True

        messages.error(request, 'Your page was not found')
        return redirect('index')

    # finalListing = None

    # listings = list(chain(OwnerModel.objects.order_by('-listDate').filter(propertyStatus='Available'), PropertyBrandsModel.objects.order_by('-listDate').filter(propertyStatus='Available')))

    # for i in listings:
    #     if i.whatsapp == whatsapp:
    #         finalListing = i
    #         break

    # if finalListing:
    #     context = {
    #             'listing': finalListing,
    #     }
    #     return render(request, 'listings/listing.html', context)
    # else:
    #     storage = messages.get_messages(request)
    #     storage.used = True

    #     messages.error(request, 'Your page was not found')
    #     return redirect('index')

def howItWorks(request):
    return render(request, 'pages/howItWorks.html')

def comingSoon(request):
    return render(request, 'pages/comingSoon.html')

def loaderIO2(request):
    return render(request, 'pages/loaderio-003734d6f270f6f6a577843a18e13526.txt')