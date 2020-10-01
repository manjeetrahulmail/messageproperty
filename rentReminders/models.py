from django.db import models

# Create your models here.
class Tenant(models.Model):

    name = models.CharField(verbose_name="User's Name", max_length=50)
    userEmail = models.EmailField(verbose_name="User's Email Address", max_length=60)
    whatsapp = models.CharField(verbose_name="User's Whatsapp Number", max_length=10)
    tenantEmail = models.EmailField(verbose_name="Tenant's Email Address", max_length=60)
    listDate = models.DateTimeField(verbose_name='Reminder Set On', auto_now=True)