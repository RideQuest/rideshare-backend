from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField


CAR_BRAND = [('Audi', 'Audi'), ('Acura', 'Acura'), ('BMW', 'BMW'),
             ('Buick', 'Buick'), ('Cadillac', 'Cadillac'),
             ('Chevrolet', 'Chevrolet'), ('Chrysler', 'Chrysler'),
             ('Citroen', 'Citroen'), ('Dodge', 'Dodge'), ('Fiat', 'Fiat'),
             ('Ford', 'Ford'), ('GMC', 'GMC'), ('Honda', 'Honda'),
             ('Hyundai', 'Hyundai'), ('Infiniti', 'Infiniti'),
             ('Jaguar', 'Jaguar'), ('Jeep', 'Jeep'), ('Kia', 'Kia'),
             ('Land Rover', 'Land Rover'), ('Lexus', 'Lexus'),
             ('Mazda', 'Mazda'), ('Mercedes-Benz', 'Mercedes-Benz'),
             ('Mitsubishi', 'Mitsubishi'), ('Nissan', 'Nissan'),
             ('Porche', 'Porche'), ('Ram', 'Ram'), ('Saab', 'Saab'),
             ('Subaru', 'Subaru'), ('Suzuki', 'Suzuki'), ('Tesla', 'Tesla'),
             ('Toyota', 'Toyota'), ('Volkswagen', 'Volkswagen'),
             ('Volvo', 'Volvo')]


class Profile(models.Model):
    """Profile class."""

    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='profile')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = PhoneNumberField(blank=True, null=True)
    car_brand = models.CharField(max_length=10, choices=CAR_BRAND, default=None)
    car_seat = models.IntegerField()
    pets_allowed = models.BooleanField()



class Route(models.Model):
    """Route model for profile."""
    # Start Address
    in_profile = models.ForeignKey(Profile,
                                   on_delete=models.CASCADE,
                                   related_name='routes')
    address_line1 = models.CharField("Start Address line 1", max_length=40)
    address_line2 = models.CharField("Start Address line 2", max_length=40,
                                     blank=True)
    postal_code = models.CharField("Start Zip Code", max_length=10)
    city = models.CharField(max_length=50)
    state = models.CharField("Start State", max_length=40)
    # Destination Address
    destination_line1 = models.CharField("Destination Address line 1",
                                         max_length=40)
    destination_line2 = models.CharField("Destination Address line 2",
                                         max_length=40, blank=True)
    destination_postal_code = models.CharField("Destination Zip Code",
                                               max_length=10)
    destination_city = models.CharField(max_length=50)
    destination_state = models.CharField("Destination State", max_length=40)
