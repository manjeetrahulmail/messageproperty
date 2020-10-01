from django.shortcuts import render, get_object_or_404
from .models import Distributor

# Create your views here.
def sale(request, username):

    distributor = get_object_or_404(Distributor, pk=username)

    context = {
        'distributor': distributor,
    }

    return render(request, 'affiliates/sale.html', context)