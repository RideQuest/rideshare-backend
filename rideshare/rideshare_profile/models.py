from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.gis.db import models as geomodels


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


class Route(geomodels.Model):
    """Route model for profile."""
    # Start Address
    in_profile = models.ForeignKey(Profile,
                                   on_delete=models.CASCADE,
                                   related_name='routes')
    point = geomodels.PointField()
