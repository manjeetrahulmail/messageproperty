from django.contrib import admin

from .models import Tenant

# Register your models here.
class TenantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'userEmail', 'whatsapp', 'tenantEmail', 'listDate')
    list_display_links = ('id',)
    search_fields = ('name', 'userEmail', 'whatsapp', 'tenantEmail')

admin.site.register(Tenant, TenantAdmin)