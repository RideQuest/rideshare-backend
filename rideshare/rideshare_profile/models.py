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


def upload_to(instance, filename):
    """Return path to media files."""
    return 'avatars/{}/{}'.format(instance.profile.id, filename)


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

    def __str__(self):
        """String representation of user."""
        return '{}'.format(self.user.username)


class Avatar(models.Model):
    """Avatar class."""

    profile = models.OneToOneField(Profile,
                                   on_delete=models.CASCADE,
                                   related_name='avatar')
    image_url = models.ImageField(blank=True, null=True, upload_to=upload_to)


class Route(geomodels.Model):
    """Route model for profile."""

    user = geomodels.ForeignKey(Profile,
                                on_delete=models.CASCADE,
                                related_name='routes')
    start_point = geomodels.PointField(default='')
