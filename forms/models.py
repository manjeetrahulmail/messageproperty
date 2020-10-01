from django.db import models

from datetime import datetime

# Create your models here.
class OwnerModel(models.Model):

    connectionType = models.CharField(max_length=30)
    offerType = models.CharField(max_length=10)
    propertyType = models.CharField(max_length=10)
    propertyStatus = models.CharField(max_length=15)
    price = models.PositiveIntegerField()
    locality = models.CharField(max_length=35)
    city = models.CharField(max_length=85)

    media = models.CharField(blank=True, max_length=150)
    sqft = models.CharField(blank=True, max_length=10)
    floorNumber = models.CharField(blank=True, max_length=2)
    gatedCommunity = models.CharField(max_length=3)
    
    description = models.TextField(max_length=300, blank=True)
    name = models.CharField(max_length=50)
    whatsapp = models.CharField(max_length=10)

    isVerified = models.BooleanField(default=False)
    listDate = models.DateTimeField(auto_now_add=True)
    lastEdited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name+' : '+self.whatsapp

class PropertyBrandsModel(models.Model):
    
    connectionType = models.CharField(max_length=30)
    offerType = models.CharField(max_length=10)
    
    one_bhk = models.BooleanField(default=False)
    two_bhk = models.BooleanField(default=False)
    three_bhk = models.BooleanField(default=False)
    four_bhk = models.BooleanField(default=False)
    fivePlus_bhk = models.BooleanField(default=False)

    numPropertyType = models.IntegerField(default=0)

    propertyStatus = models.CharField(max_length=15)
    price = models.PositiveIntegerField(default=0)
    locality = models.CharField(max_length=35)
    city = models.CharField(max_length=85)
    description = models.TextField(max_length=300)
    name = models.CharField(max_length=50)
    whatsapp = models.CharField(max_length=10)
    
    isVerified = models.BooleanField(default=False)
    listDate = models.DateTimeField(auto_now_add=True)
    lastEdited = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name+' : '+self.whatsapp


class Report (models.Model):

    reportContent = models.TextField(max_length=300)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=10)
    reportDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Whatsapp - " + self.whatsapp + ", Email - " + self.email
    

class EditListing (models.Model):

    content = models.TextField(max_length=300)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=10)
    reportDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Whatsapp - " + self.whatsapp + ", Email - " + self.email


class Requirement(models.Model):

    content = models.TextField(max_length=300)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=10)
    reportDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Whatsapp - " + self.whatsapp + ", Email - " + self.email