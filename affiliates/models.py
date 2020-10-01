from django.db import models

# Create your models here.
class Distributor(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    father_name = models.CharField(max_length=50)

    locality = models.CharField(max_length=35)
    city = models.CharField(max_length=85)

    link1 = models.CharField(max_length=50, blank=True)
    link2 = models.CharField(max_length=50, blank=True)
    link3 = models.CharField(max_length=50, blank=True)
    link4 = models.CharField(max_length=50, blank=True)
    link5 = models.CharField(max_length=50, blank=True)

    dob = models.DateField()
    
    username = models.CharField(max_length=50, primary_key=True, unique=True)
    whatsapp = models.CharField(max_length=10)

    brand_name = models.CharField(max_length=50, blank=True)
