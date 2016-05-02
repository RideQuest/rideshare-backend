from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField


CAR_BRAND = [('Audi', 'Audi'), ('Acura', 'Acura'), ('BMW', 'BMW')]


class Profile(models.Model):
    """Profile class."""

    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='profile')
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phonenumber = PhoneNumberField(blank=True, null=True)
    carbrand = models.CharField(max_length=10, choices=CAR_BRAND, default=None)
    carseat = models.IntegerField()
    petsallowed = models.BooleanField()

    # def __str__(self):
    #     return self.user


class Route(models.Model):
    # Start Address
    in_profile = models.ForeignKey(Profile,
                                   on_delete=models.CASCADE,
                                   related_name='routes')
    address_line1 = models.CharField("Address line 1", max_length=40)
    address_line2 = models.CharField("Address line 2", max_length=40, blank=True)
    postal_code = models.CharField("Zip Code", max_length=10)
    city = models.CharField(max_length=50)
    state = models.CharField("State", max_length=40)
    # Destination Address
    destination_line1 = models.CharField("Address line 1", max_length=40)
    destination_line2 = models.CharField("Address line 2", max_length=40, blank=True)
    destination_postal_code = models.CharField("Zip Code", max_length=10)
    destination_city = models.CharField(max_length=50)
    destination_state = models.CharField("State", max_length=40)


    # def __str__(self):
    #     return self.in_profile
