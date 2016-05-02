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
    carseat = models.IntegerField(max_length=2)
    petsallowed = models.BooleanField()

    def __str__(self):
        return self.user
