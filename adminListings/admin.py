from django.contrib import admin

from .models import AdminListing

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id',  'name', 'whatsapp', 'isVerified', 'propertyStatus', 'listDate')
    list_display_links = ('id', 'name', 'whatsapp')
    list_editable = ('isVerified',)
    search_fields = ('name', 'whatsapp')

admin.site.register(AdminListing, ListingAdmin)