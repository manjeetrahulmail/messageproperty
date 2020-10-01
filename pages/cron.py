from rentReminders.models import Tenant

from django.conf import settings
from django.core.mail import EmailMessage

tenants = Tenant.objects.order_by('-listDate')

# userEmails = []
# tenantEmails = []

# for tenant in tenants:
#     userEmails.append(tenant.userEmail)
#     tenantEmails.append(tenant.tenantEmail)

def send_tenant_emails():

    if tenants:
        for tenant in tenants:
            email = EmailMessage(
                'Rent Reminder from messageproperty.com',

                'This is an automatic reminder for the payment of the rent for the property id : https://www.messageproperty.com/' + tenant.whatsapp + '\n\nYou can pay the rent as per agreed upon T&C with your owner.\n\nYou are getting this email as your owner uses messageproperty.com rent reminder service for his property.\n\nIf paid already, kindly ignore . ',

                settings.EMAIL_HOST_USER,
                [tenant.tenantEmail]
            )
            email.send()

def send_owner_emails():

    if tenants:
        for tenant in tenants:
            email = EmailMessage(
                'Rent Reminder sent to your tenant by messageproperty.com',

                'This is an automatic email which is generated to inform you that an email of rent reminder was sent to your tenant for the property profile : https://www.messageproperty.com/' + tenant.whatsapp + '\n\nTo get your home rented, sold, painted, cleaned or for any such kind of handyman services, kindly visit https://www.messageproperty.com',

                settings.EMAIL_HOST_USER,
                [tenant.userEmail]
            )
            email.send()