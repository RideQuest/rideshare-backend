"""Test User, Profile and model."""
from django.test import TestCase, Client
from .models import Profile, Route
from django.contrib.auth.models import User
# from django.contrib.gis.geos import GEOSGeometry


class TestProfile(TestCase):
    """Test profile functionality."""

    def setUp(self):
        """Test new user creation."""
        self.client = Client()

        self.test_user_1 = User.objects.create_user('driver1')
        self.test_user_2 = User.objects.create_user('rider1')
        self.test_user_3 = User.objects.create_user(username='Dear Test', password='pycov')
        self.test_profile_1 = Profile()
        self.test_profile_2 = Profile()
        self.test_profile_3 = Profile()
        self.test_profile_1.user = self.test_user_1
        self.test_profile_2.user = self.test_user_2
        self.test_profile_3.user = self.test_user_3
        self.test_profile_1.carbrand = 'Audi'
        self.test_profile_2.carbrand = 'Audi'
        self.test_profile_3.carbrand = 'Audi'
        self.test_profile_1.carseat = 3
        self.test_profile_2.carseat = 3
        self.test_profile_3.carseat = 3
        self.test_profile_1.petsallowed = True
        self.test_profile_2.petsallowed = True
        self.test_profile_3.petsallowed = True
        self.test_profile_1.save()
        self.test_profile_2.save()
        self.test_profile_3.save()
        # self.test_route_1 = Route()
        # self.test_route_2 = Route()
        # self.test_route_3 = Route()
        # self.test_route_1.user = self.test_profile_1
        # self.test_route_2.user = self.test_profile_2
        # self.test_route_3.user = self.test_profile_3
        # self.test_route_1.geoCoords = GEOSGeometry('POINT(1 2)', srid=4326)
        # self.test_route_2.geoCoords = GEOSGeometry('POINT(1 2)', srid=4326)
        # self.test_route_3.geoCoords = GEOSGeometry('POINT(1 2)', srid=4326)
        # self.test_route_1.save()
        # self.test_route_2.save()
        # self.test_route_3.save()

    def test_verify_save(self):
        """Test user saved ."""
        self.assertEquals(len(User.objects.all()), 3)

    def test_profile_count(self):
        self.assertEquals(len(Profile.objects.all()), 3)

    # def test_route_count(self):
    #     self.assertEquals(len(Route.objects.all()), 3)



