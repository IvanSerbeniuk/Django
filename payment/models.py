from django.db import models

from django.contrib.auth.models import User

class ShippingAddress(models.Model):

    full_name = models.CharField(max_length=150)

    email = models.EmailField(max_length=255)

    address1 = models.CharField(max_length=150)

    address2 = models.CharField(max_length=150)

    city = models.CharField(max_length=255)

    
    # Optional
    state = models.CharField(max_length=255, null=True, blank=True)# Null for our database. Blank for user side 

    zipcode = models.CharField(max_length=255, null=True, blank=True)

    # Foreign Key
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) #on_delete - when user deletes his account then shipping informaton also will be removedx

    class Meta:

        verbose_name_plural = 'Shipping Address'

    
    def __str__(self):

        return 'Shipping Address - ' + str(self.id)