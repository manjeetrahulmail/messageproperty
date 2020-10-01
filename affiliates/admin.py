from django.contrib import admin
from .models import Distributor

# Register your models here.
class DistributorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

admin.site.register(Distributor, DistributorAdmin)