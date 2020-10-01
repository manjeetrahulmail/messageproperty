from django.shortcuts import render, redirect, get_object_or_404
from .models import OwnerModel, PropertyBrandsModel, Report, EditListing, Requirement
from django.contrib import messages

import requests
import json

from adminListings.models import AdminListing

# Create your views here.
def ownerForm(request):

    if request.user.is_authenticated:

        if request.method == 'POST':

            connectionType = request.POST['connectionType']
            offerType = request.POST['offerType']
            propertyType = request.POST['propertyType']
            propertyStatus = request.POST['propertyStatus']
            price = request.POST['price']
            locality = request.POST['locality']
            city = request.POST['city']
            if 'media' in request.POST:
                media = request.POST['media']
            if 'sqft' in request.POST:
                sqft = request.POST['sqft']
            floorNumber = 0
            if 'floorNumber' in request.POST:
                floorNumber = request.POST['floorNumber']
            gatedCommunity = request.POST['gatedCommunity']
            if 'description' in request.POST:
                description = request.POST['description']
            name = request.POST['userName']
            whatsapp = request.POST['whatsapp']

            clientKey = request.POST['g-recaptcha-response']
            secretKey = '6LeB18MZAAAAACGvnBPchyvG0rIje6d9aGHpTHzX'

            captchaData = {
                'secret': secretKey,
                'response': clientKey,
            }

            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=captchaData)
            response = json.loads(r.text)

            if response['success']:

                if  not price.isdigit() or int(price) <= 0:
                    storage = messages.get_messages(request)
                    storage.used = True

                    messages.error(request, 'Property price cannot be negative or 0')
                    return redirect('ownerForm')

                if sqft != '':
                    if not sqft.isdigit() or int(sqft) <= 0:
                        storage = messages.get_messages(request)
                        storage.used = True

                        messages.error(request, 'Sqft Area cannot be negative or 0')
                        return redirect('ownerForm')

                if floorNumber != '':
                    if  not floorNumber.isdigit() or int(floorNumber) < 0 or int(floorNumber) > 99:
                        storage = messages.get_messages(request)
                        storage.used = True

                        messages.error(request, 'You have entered an invalid floor number')
                        return redirect('ownerForm')

                if  len(whatsapp) != 10 or not whatsapp.isdigit() or int(whatsapp) < 0:
                    storage = messages.get_messages(request)
                    storage.used = True

                    messages.error(request, 'Enter a valid whatsapp number without (+91) or (0)')
                    return redirect('ownerForm')

                if OwnerModel.objects.filter(whatsapp=whatsapp).exists() or PropertyBrandsModel.objects.filter(whatsapp=whatsapp).exists():
                    storage = messages.get_messages(request)
                    storage.used = True

                    messages.error(request, 'We have already recieved a request from your number')
                    return redirect('ownerForm')

                ownerListing = OwnerModel(connectionType=connectionType, offerType=offerType, propertyType=propertyType, propertyStatus=propertyStatus, price=price, locality=locality, city=city, media=media, sqft=sqft,  floorNumber=floorNumber, gatedCommunity=gatedCommunity, description=description, name=name, whatsapp=whatsapp)

                ownerListing.save()

                storage = messages.get_messages(request)
                storage.used = True

                myLink = 'https://www.messageproperty.com/' + whatsapp
                messages.success(request, 'Your request is submitted')

                # messages.success(request, '<strong>Go to your listing : </strong><a href="' + myLink + '"><u>Click Here</u></a>', extra_tags='safe')

                messages.success(request, '<strong>For home services(paint,clean,pest) : </strong><a href="https://wa.me/919108095640?text=I%20want%20home%20services%20from%20messageproperty.com%20for%20my%20listing."><u>Click Here</u></a>', extra_tags='safe')

                return redirect('dashboard')
            else:
                storage = messages.get_messages(request)
                storage.used = True

                messages.error(request, "Invalid Captcha")
                return redirect('dashboard')

        return render(request, 'forms/ownerForm.html')
    else:
        storage = messages.get_messages(request)
        storage.used = True

        messages.error(request, "You must login to access the requested page")
        return redirect('index')

def propertyBrandsForm(request):

    if request.user.is_authenticated:

        if request.method == 'POST':

            numPropertyType = 0

            connectionType = request.POST['connectionType']
            offerType = request.POST['offerType']

            one_bhk = False
            two_bhk = False
            three_bhk = False
            four_bhk = False
            fivePlus_bhk = False

            if 'one_bhk' in request.POST and request.POST['one_bhk'] == 'on':
                one_bhk = True
                numPropertyType += 1
            if 'two_bhk' in request.POST and request.POST['two_bhk'] == 'on':
                two_bhk = True
                numPropertyType += 1
            if 'three_bhk' in request.POST and request.POST['three_bhk'] == 'on':
                three_bhk = True
                numPropertyType += 1
            if 'four_bhk' in request.POST and request.POST['four_bhk'] == 'on':
                four_bhk = True
                numPropertyType += 1
            if 'fivePlus_bhk' in request.POST and request.POST['fivePlus_bhk'] == 'on':
                fivePlus_bhk = True
                numPropertyType += 1

            propertyStatus = request.POST['propertyStatus']
            if 'price' in request.POST and request.POST['price']:
                price = request.POST['price']
            else:
                price = 0
            locality = request.POST['locality']
            city = request.POST['city']
            description = request.POST['description']
            name = request.POST['userName']
            whatsapp = request.POST['whatsapp']

            clientKey = request.POST['g-recaptcha-response']
            secretKey = '6LeB18MZAAAAACGvnBPchyvG0rIje6d9aGHpTHzX'

            captchaData = {
                'secret': secretKey,
                'response': clientKey,
            }

            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=captchaData)
            response = json.loads(r.text)

            if response['success']:

                if price != 0:
                    if not price.isdigit() or int(price) < 0:
                        storage = messages.get_messages(request)
                        storage.used = True

                        messages.error(request, 'Property price cannot be negative')
                        return redirect('propertyBrandsForm')

                if  len(whatsapp) != 10 or not whatsapp.isdigit() or int(whatsapp) < 0:
                    storage = messages.get_messages(request)
                    storage.used = True

                    messages.error(request, 'Enter a valid whatsapp number without (+91) or (0)')
                    return redirect('propertyBrandsForm')

                if OwnerModel.objects.filter(whatsapp=whatsapp).exists() or PropertyBrandsModel.objects.filter(whatsapp=whatsapp).exists():
                    storage = messages.get_messages(request)
                    storage.used = True

                    messages.error(request, 'We have already recieved a request from your number')
                    return redirect('propertyBrandsForm')

                propertyBrandListings = PropertyBrandsModel(connectionType=connectionType, offerType=offerType, one_bhk=one_bhk, two_bhk=two_bhk, three_bhk=three_bhk, four_bhk=four_bhk, fivePlus_bhk=fivePlus_bhk, numPropertyType=numPropertyType - 1, propertyStatus=propertyStatus, price=price, locality=locality, city=city, description=description, name=name, whatsapp=whatsapp)

                propertyBrandListings.save()

                storage = messages.get_messages(request)
                storage.used = True

                myLink = 'https://www.messageproperty.com/' + whatsapp
                messages.success(request, 'Your request is submitted')
                # messages.success(request, '<strong>Go to your listing : </strong><a href="' + myLink + '"><u>Click Here</u></a>', extra_tags='safe')
                return redirect('dashboard')

            else:
                storage = messages.get_messages(request)
                storage.used = True

                messages.error(request, "Invalid Captcha")
                return redirect('propertyBrandsForm')

        return render(request, 'forms/propertyBrandsForm.html')
    else:
        storage = messages.get_messages(request)
        storage.used = True

        messages.error(request, "You must login to access the requested page")
        return redirect('index')

def report(request):

    if request.method == 'POST':
        reportContent = request.POST['reportContent']
        email = request.POST['email']
        whatsapp = request.POST['whatsapp']

        clientKey = request.POST['g-recaptcha-response']
        secretKey = '6LeB18MZAAAAACGvnBPchyvG0rIje6d9aGHpTHzX'

        captchaData = {
            'secret': secretKey,
            'response': clientKey,
        }

        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=captchaData)
        response = json.loads(r.text)

        if response['success']:

            report = Report(reportContent=reportContent, email=email, whatsapp=whatsapp)
            report.save()

            storage = messages.get_messages(request)
            storage.used = True

            messages.success(request, 'Your request is submitted')
            return redirect('index')

        else:
            storage = messages.get_messages(request)
            storage.used = True

            messages.error(request, "Invalid Captcha")
            return redirect('report')

    return render(request, 'forms/report.html')

def editListing(request):

    if request.method == 'POST':
        content = request.POST['content']
        email = request.POST['email']
        whatsapp = request.POST['whatsapp']

        clientKey = request.POST['g-recaptcha-response']
        secretKey = '6LeB18MZAAAAACGvnBPchyvG0rIje6d9aGHpTHzX'

        captchaData = {
            'secret': secretKey,
            'response': clientKey,
        }

        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=captchaData)
        response = json.loads(r.text)

        if response['success']:

            editRequest = EditListing(content=content, email=email, whatsapp=whatsapp)
            editRequest.save()

            storage = messages.get_messages(request)
            storage.used = True

            messages.success(request, 'Your request is submitted')
            return redirect('index')

        else:
            storage = messages.get_messages(request)
            storage.used = True

            messages.error(request, "Invalid Captcha")
            return redirect('editListing')

    return render(request, 'forms/editListing.html')

def requirements(request):

    if request.method == 'POST':
        content = request.POST['content']
        email = request.POST['email']
        whatsapp = request.POST['whatsapp']

        clientKey = request.POST['g-recaptcha-response']
        secretKey = '6LeB18MZAAAAACGvnBPchyvG0rIje6d9aGHpTHzX'

        captchaData = {
            'secret': secretKey,
            'response': clientKey,
        }

        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=captchaData)
        response = json.loads(r.text)

        if response['success']:

            requirementsRequest = Requirement(content=content, email=email, whatsapp=whatsapp)
            requirementsRequest.save()

            storage = messages.get_messages(request)
            storage.used = True

            messages.success(request, 'Your request is submitted')
            return redirect('index')

        else:
            storage = messages.get_messages(request)
            storage.used = True

            messages.error(request, "Invalid Captcha")
            return redirect('editListing')

    return render(request, 'forms/requirements.html')

def editOwnerListing(request):

    if request.user.is_authenticated:

        whatsapp = request.user.whatsapp
        listing = get_object_or_404(OwnerModel, whatsapp=whatsapp)

        if request.method == 'POST':

            connectionType = request.POST['connectionType']
            offerType = request.POST['offerType']
            propertyType = request.POST['propertyType']
            # propertyStatus = request.POST['propertyStatus']
            price = request.POST['price']
            locality = request.POST['locality']
            city = request.POST['city']
            if 'media' in request.POST:
                media = request.POST['media']
            if 'sqft' in request.POST:
                sqft = request.POST['sqft']
            floorNumber = 0
            if 'floorNumber' in request.POST:
                floorNumber = request.POST['floorNumber']
            gatedCommunity = request.POST['gatedCommunity']
            if 'description' in request.POST:
                description = request.POST['description']
            name = request.POST['userName']

            clientKey = request.POST['g-recaptcha-response']
            secretKey = '6LeB18MZAAAAACGvnBPchyvG0rIje6d9aGHpTHzX'

            captchaData = {
                'secret': secretKey,
                'response': clientKey,
            }

            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=captchaData)
            response = json.loads(r.text)

            if response['success']:

                if not price.isdigit() or int(price) <= 0:
                    storage = messages.get_messages(request)
                    storage.used = True

                    messages.error(request, 'Property price cannot be negative or 0')
                    return redirect('editOwnerListing')

                if sqft != '':
                    if not sqft.isdigit() or int(sqft) <= 0 :
                        storage = messages.get_messages(request)
                        storage.used = True

                        messages.error(request, 'Sqft Area cannot be negative or 0')
                        return redirect('editOwnerListing')

                if floorNumber != '':
                    if  not floorNumber.isdigit() or int(floorNumber) < 0 or int(floorNumber) > 99:
                        storage = messages.get_messages(request)
                        storage.used = True

                        messages.error(request, 'You have entered an invalid floor number')
                        return redirect('editOwnerListing')

                listing.connectionType = connectionType
                listing.offerType = offerType
                listing.propertyType = propertyType
                # listing.propertyStatus = propertyStatus
                listing.price = price
                listing.locality = locality
                listing.city = city
                listing.media = media
                listing.sqft = sqft
                listing.floorNumber = floorNumber
                listing.gatedCommunity = gatedCommunity
                listing.description = description
                listing.name = name


                listing.save()

                storage = messages.get_messages(request)
                storage.used = True

                myLink = 'https://www.messageproperty.com/' + whatsapp
                messages.success(request, 'Your request is submitted')
                messages.success(request, '<strong>Go to your listing : </strong><a href="' + myLink + '"><u>Click Here</u></a>', extra_tags='safe')
                messages.success(request, '<strong>For home services(paint,clean,pest) : </strong><a href="https://wa.me/919108095640?text=I%20want%20home%20services%20from%20messageproperty.com%20for%20my%20listing."><u>Click Here</u></a>', extra_tags='safe')
                return redirect('dashboard')

            else:
                storage = messages.get_messages(request)
                storage.used = True

                messages.error(request, "Invalid Captcha")
                return redirect('editOwnerListing')

        context = {
            'listing':listing,
        }

        return render(request, 'forms/ownerForm.html', context)
    else:
        storage = messages.get_messages(request)
        storage.used = True

        messages.error(request, "You are not authorized to access messageproperty.com/forms/edit-owner-property")
        return redirect('index')

def editPropertyBrandsListing(request):

    if request.user.is_authenticated:

        whatsapp = request.user.whatsapp
        listing = get_object_or_404(PropertyBrandsModel, whatsapp=whatsapp)

        if request.method == 'POST':

            numPropertyType = 0

            connectionType = request.POST['connectionType']
            offerType = request.POST['offerType']

            one_bhk = False
            two_bhk = False
            three_bhk = False
            four_bhk = False
            fivePlus_bhk = False

            if 'one_bhk' in request.POST and request.POST['one_bhk'] == 'on':
                one_bhk = True
                numPropertyType += 1
            if 'two_bhk' in request.POST and request.POST['two_bhk'] == 'on':
                two_bhk = True
                numPropertyType += 1
            if 'three_bhk' in request.POST and request.POST['three_bhk'] == 'on':
                three_bhk = True
                numPropertyType += 1
            if 'four_bhk' in request.POST and request.POST['four_bhk'] == 'on':
                four_bhk = True
                numPropertyType += 1
            if 'fivePlus_bhk' in request.POST and request.POST['fivePlus_bhk'] == 'on':
                fivePlus_bhk = True
                numPropertyType += 1

            propertyStatus = request.POST['propertyStatus']
            if 'price' in request.POST and request.POST['price']:
                price = request.POST['price']
            else:
                price = 0
            locality = request.POST['locality']
            city = request.POST['city']
            description = request.POST['description']
            name = request.POST['userName']

            clientKey = request.POST['g-recaptcha-response']
            secretKey = '6LeB18MZAAAAACGvnBPchyvG0rIje6d9aGHpTHzX'

            captchaData = {
                'secret': secretKey,
                'response': clientKey,
            }

            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=captchaData)
            response = json.loads(r.text)

            if response['success']:

                if price != 0:
                    if not price.isdigit() or int(price) < 0:
                        storage = messages.get_messages(request)
                        storage.used = True

                        messages.error(request, 'Property price cannot be negative')
                        return redirect('editPropertyBrandsListing')

                listing.connectionType = connectionType
                listing.offerType = offerType

                listing.one_bhk = one_bhk
                listing.two_bhk = two_bhk
                listing.three_bhk = three_bhk
                listing.four_bhk = four_bhk
                listing.fivePlus_bhk = fivePlus_bhk

                listing.numPropertyType = numPropertyType - 1

                listing.propertyStatus = propertyStatus
                listing.price = price
                listing.locality = locality
                listing.city = city
                listing.description = description
                listing.name = name

                listing.save()

                storage = messages.get_messages(request)
                storage.used = True

                myLink = 'https://www.messageproperty.com/' + whatsapp
                messages.success(request, 'Your request is submitted')
                messages.success(request, '<strong>Go to your listing : </strong><a href="' + myLink + '"><u>Click Here</u></a>', extra_tags='safe')
                return redirect('dashboard')

            else:
                storage = messages.get_messages(request)
                storage.used = True

                messages.error(request, "Invalid Captcha")
                return redirect('editPropertyBrandsListing')

        context = {
            'listing':listing,
        }

        return render(request, 'forms/propertyBrandsForm.html', context)
    else:
        storage = messages.get_messages(request)
        storage.used = True

        messages.error(request, "You are not authorized to access messageproperty.com/forms/edit-property-brands-listing")
        return redirect('index')

def editAdminListing(request, listing_id):

    if request.user.is_authenticated:

        listing = get_object_or_404(AdminListing, id=listing_id)

        if request.method == 'POST':

            numPropertyType = 0

            connectionType = request.POST['connectionType']
            offerType = request.POST['offerType']

            one_bhk = False
            two_bhk = False
            three_bhk = False
            four_bhk = False
            fivePlus_bhk = False

            if 'one_bhk' in request.POST and request.POST['one_bhk'] == 'on':
                one_bhk = True
                numPropertyType += 1
            if 'two_bhk' in request.POST and request.POST['two_bhk'] == 'on':
                two_bhk = True
                numPropertyType += 1
            if 'three_bhk' in request.POST and request.POST['three_bhk'] == 'on':
                three_bhk = True
                numPropertyType += 1
            if 'four_bhk' in request.POST and request.POST['four_bhk'] == 'on':
                four_bhk = True
                numPropertyType += 1
            if 'fivePlus_bhk' in request.POST and request.POST['fivePlus_bhk'] == 'on':
                fivePlus_bhk = True
                numPropertyType += 1

            propertyStatus = request.POST['propertyStatus']
            if 'price' in request.POST and request.POST['price']:
                price = request.POST['price']
            else:
                price = 0
            locality = request.POST['locality']
            city = request.POST['city']

            if 'media' in request.POST:
                media = request.POST['media']
            if 'sqft' in request.POST:
                sqft = request.POST['sqft']
            floorNumber = 0
            if 'floorNumber' in request.POST:
                floorNumber = request.POST['floorNumber']
            if 'gatedCommunity' in request.POST:
                gatedCommunity = request.POST['gatedCommunity']
            if 'description' in request.POST:
                description = request.POST['description']

            name = request.POST['userName']

            clientKey = request.POST['g-recaptcha-response']
            secretKey = '6LeB18MZAAAAACGvnBPchyvG0rIje6d9aGHpTHzX'

            captchaData = {
                'secret': secretKey,
                'response': clientKey,
            }

            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=captchaData)
            response = json.loads(r.text)

            if response['success']:

                if price != 0:
                    if  not price.isdigit() or int(price) <= 0:
                        storage = messages.get_messages(request)
                        storage.used = True

                        messages.error(request, 'Property price cannot be negative or 0')
                        return redirect('editAdminListing')

                if sqft != '':
                    if  not sqft.isdigit() or int(sqft) <= 0:
                        storage = messages.get_messages(request)
                        storage.used = True

                        messages.error(request, 'Sqft Area cannot be negative or 0')
                        return redirect('editAdminListing')

                if floorNumber != '':
                    if   not floorNumber.isdigit() or int(floorNumber) < 0 or int(floorNumber) > 99:
                        storage = messages.get_messages(request)
                        storage.used = True

                        messages.error(request, 'You have entered an invalid floor number')
                        return redirect('editAdminListing')

                listing.connectionType = connectionType
                listing.offerType = offerType

                listing.one_bhk = one_bhk
                listing.two_bhk = two_bhk
                listing.three_bhk = three_bhk
                listing.four_bhk = four_bhk
                listing.fivePlus_bhk = fivePlus_bhk

                listing.numPropertyType = numPropertyType - 1

                listing.propertyStatus = propertyStatus
                listing.price = price
                listing.locality = locality
                listing.city = city

                listing.media = media
                listing.sqft = sqft
                listing.floorNumber = floorNumber
                listing.gatedCommunity = gatedCommunity

                listing.description = description
                listing.name = name

                listing.save()

                storage = messages.get_messages(request)
                storage.used = True

                myLink = 'https://www.messageproperty.com/main/' + str(listing_id)
                messages.success(request, 'Your request is submitted')
                messages.success(request, '<strong>Go to your listing : </strong><a href="' + myLink+ '"><u>Click Here</u></a>', extra_tags='safe')
                return redirect('dashboard')

            else:
                storage = messages.get_messages(request)
                storage.used = True

                messages.error(request, "Invalid Captcha")
                return redirect('editAdminListing', listing_id)

        context = {
            'listing':listing,
        }

        return render(request, 'forms/editAdminListing.html', context)
    else:
        storage = messages.get_messages(request)
        storage.used = True

        messages.error(request, "You are not authorized to access messageproperty.com/forms/edit-main-" + listing_id)
        return redirect('index')