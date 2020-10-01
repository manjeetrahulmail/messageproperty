from django.contrib import admin

from .models import Account
# from django.contrib.auth.admin import UserAdmin

# class AccountAdmin(UserAdmin):
#     list_display = ('first_name', 'last_name', 'email', 'whatsapp', 'clicks', 'date_joined', 'last_login', 'is_admin')
#     search_fields = ('first_name', 'last_name', 'email', 'whatsapp')
#     readonly_fields = ('date_joined', 'last_login')

#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()

#     ordering = ()

# # Register your models here.
admin.site.register(Account)