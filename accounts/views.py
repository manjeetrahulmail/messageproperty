from django.shortcuts import render, redirect, get_object_or_404

from accounts.models import Account
from django.contrib import messages
from django.contrib import auth

from forms.models import OwnerModel, PropertyBrandsModel
from itertools import chain

from adminListings.models import AdminListing

# Create your views here.
def login(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)

            storage = messages.get_messages(request)
            storage.used = True

            messages.success(request, 'You are now logged in')

            messages.success(request, "Your property link will be in format of messageproperty.com/whatsapp number,once posted it can be easily remembered to share with anyone.", extra_tags='safe')

            # messages.success(request, 'For updates on whatsapp <a href="https://wa.me/919108095640?text=I%20want%20updates%20from%20messageproperty.com%20on%20whatsapp%20for%20my%20listing.">Click Here</a>', extra_tags='safe')
            return redirect('dashboard')
        else:
            storage = messages.get_messages(request)
            storage.used = True

            messages.error(request, 'Invalid Credentials')
            return redirect('login')

    if request.user.is_authenticated:
        return redirect('dashboard')

    return render(request, 'accounts/login.html')

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        whatsapp = request.POST['whatsapp']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            storage = messages.get_messages(request)
            storage.used = True

            messages.error(request, 'Passwords do not match')
            return redirect('register')
        else:
            if Account.objects.filter(email=email).exists():

                storage = messages.get_messages(request)
                storage.used = True

                messages.error(request, 'Email is already registered')
                return redirect('register')
            else:
                if Account.objects.filter(whatsapp=whatsapp).exists():

                    storage = messages.get_messages(request)
                    storage.used = True

                    messages.error(request, 'Whatsapp Number is already registered')
                    return redirect('register')
                else:
                    if  len(whatsapp) != 10 or not whatsapp.isdigit() or int(whatsapp) < 0:
                        storage = messages.get_messages(request)
                        storage.used = True

                        messages.error(request, 'Enter a valid whatsapp number without (+91) or (0)')
                        return redirect('register')
                    else:
                        account = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, whatsapp=whatsapp, password=password)
                        account.save()

                        storage = messages.get_messages(request)
                        storage.used = True

                        messages.success(request, 'Your account is created. login with your credentials')
                        return redirect('login')

    return render(request, 'accounts/register.html')

def dashboard(request):

    if request.user.is_authenticated:
        whatsapp = request.user.whatsapp
        userListing = []
        listings = list(chain(OwnerModel.objects.order_by('-listDate'), PropertyBrandsModel.objects.order_by('-listDate')))

        for listing in listings:
            if listing.whatsapp == whatsapp:
                userListing.append(listing)
                break

        adminListings = AdminListing.objects.order_by('-listDate').filter(whatsapp=whatsapp)

        # owner = OwnerModel.objects.filter(whatsapp=whatsapp).exists()
        # if owner:
        #     listing = get_object_or_404(OwnerModel, whatsapp=whatsapp)
        # else:
        #     listing = get_object_or_404(PropertyBrandsModel, whatsapp=whatsapp)

        context = {
            'userListing': userListing,
            'adminListings': adminListings,
        }

        return render(request, 'accounts/dashboard.html', context)
    else:
        return render(request, 'accounts/dashboard.html')


def logout(request):

    if request.method == 'POST':
        auth.logout(request)

        storage = messages.get_messages(request)
        storage.used = True

        messages.success(request, 'Your are now logged out')
        return redirect('index')

    return redirect('index')
