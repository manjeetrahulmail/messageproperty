from django.shortcuts import render

from accounts.models import Account
from django.conf import settings
from django.core.mail import EmailMessage

from forms.models import OwnerModel

from rentReminders.models import Tenant

# Create your views here.
def sendContent(request):

    if request.method == 'POST':

        msg = request.POST['message']

        owners = OwnerModel.objects.all()
        numbers = []
        users = Account.objects.all()
        emails = []

        for owner in owners:
            numbers.append(owner.whatsapp)

        for user in users:
            if user.whatsapp in numbers:
                emails.append(user.email)

        email = EmailMessage(
            'Asset Builder',
            msg,
            settings.EMAIL_HOST_USER,
            emails
        )
        email.fail_silently = True
        email.send()


    return render(request, 'sendContent/sendContent.html')

tenants = Tenant.objects.order_by('-listDate')

def send_tenant_emails(request):

    if tenants:
        for tenant in tenants:
            email = EmailMessage(
                'Rent Reminder from messageproperty.com',

                'This is an automatic reminder for the payment of the rent for the property id : https://www.messageproperty.com/' + tenant.whatsapp + '\n\nYou can pay the rent as per agreed upon T&C with your owner.\n\nYou are getting this email as your owner uses messageproperty.com rent reminder service for his property.\n\nIf paid already, kindly ignore . ',

                settings.EMAIL_HOST_USER,
                [tenant.tenantEmail]
            )
            email.fail_silently = True
            email.send()
    return render(request, 'pages/comingSoon.html')

def send_owner_emails(request):

    if tenants:
        for tenant in tenants:
            email = EmailMessage(
                'Rent Reminder sent to your tenant by messageproperty.com',

                'This is an automatic email which is generated to inform you that an email of rent reminder was sent to your tenant for the property profile : https://www.messageproperty.com/' + tenant.whatsapp + '\n\nTo get your home rented, sold, painted, cleaned or for any such kind of handyman services, kindly visit https://www.messageproperty.com',

                settings.EMAIL_HOST_USER,
                [tenant.userEmail]
            )
            email.fail_silently = True
            email.send()
    return render(request, 'pages/comingSoon.html')