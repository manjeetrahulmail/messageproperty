from django.shortcuts import render, redirect

from accounts.models import Account
from django.contrib import messages
from .models import Tenant

# Create your views here.
def tenantForm(request):

    if request.method == 'POST':
        name = request.POST['userName']
        userEmail = request.POST['userEmail']
        whatsapp = request.POST['whatsapp']
        tenantEmail = request.POST['tenantEmail']

        if not Account.objects.filter(whatsapp=whatsapp).exists():
            storage = messages.get_messages(request)
            storage.used = True

            messages.error(request, 'Your whatsapp number is not registered with us')
            return redirect('tenantForm')

        tenant = Tenant(name=name, userEmail=userEmail, whatsapp=whatsapp, tenantEmail=tenantEmail)
        tenant.save()

        storage = messages.get_messages(request)
        storage.used = True

        messages.success(request, 'Your reminder has been set')
        return redirect('index')

    return render(request, 'rentReminders/tenantForm.html')