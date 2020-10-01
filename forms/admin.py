from django.contrib import admin
from .models import OwnerModel, PropertyBrandsModel, Report, EditListing, Requirement


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id' ,'name', 'whatsapp', 'isVerified', 'propertyStatus', 'listDate', 'lastEdited')
    list_display_links = ('name', 'whatsapp')
    list_editable = ('isVerified',)
    search_fields = ('name', 'whatsapp')
    
class ReportAdmin(admin.ModelAdmin):
    list_display = ('whatsapp', 'email', 'reportDate')
    search_fields = ('whatsapp',)

# Register your models here.
admin.site.register(OwnerModel, ListingAdmin)
admin.site.register(PropertyBrandsModel)
admin.site.register(Report, ReportAdmin)
admin.site.register(EditListing, ReportAdmin)
admin.site.register(Requirement, ReportAdmin)