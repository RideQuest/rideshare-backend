"""Test User, Profile and model."""
from django.test import TestCase
from .models import Profile, Route
from django.contrib.auth.models import User
from django.contrib.gis.geos import GEOSGeometry


class TestProfile(TestCase):
    """Test profile functionality."""

    def setUp(self):
        """Test new profile creation."""
        self.user_1 = User.objects.create_user('driver1')
        self.user_2 = User.objects.create_user('rider1')
        self.user_3 = User.objects.create_user('rider2')

        self.profile_1 = Profile.objects.create(user=self.user_1,
                                                firstname="iwantto",
                                                lastname="addprofile",
                                                email="letmeadd@email.com",
                                                phonenumber="",
                                                carbrand="Audi",
                                                carseat=3,
                                                petsallowed="f"
                                                )
        self.profile_2 = Profile.objects.create(user=self.user_2,
                                                firstname="iwantto",
                                                lastname="addprofile",
                                                email="letmeadd@email.com",
                                                phonenumber="",
                                                carbrand="Audi",
                                                carseat=3,
                                                petsallowed="f"
                                                )
        self.profile_1.save()
        self.profile_2.save()

        self.route_1 = Route()
        self.route_2 = Route()
        self.route_1.user = self.profile_1
        self.route_2.user = self.profile_2
        self.route_1.start_point = GEOSGeometry('POINT(1 2)', srid=4326)
        self.route_2.start_point = GEOSGeometry('POINT(3 4)', srid=4326)
        self.route_1.save()
        self.route_2.save()

    def test_verify_save(self):
        """Test user saved ."""
        self.assertEquals(len(User.objects.all()), 3)

    def test_profile_count(self):
        """Test profiles saved."""
        self.assertEquals(len(Profile.objects.all()), 2)

    def test_route_count(self):
        """Test routes saved."""
        self.assertEquals(len(Route.objects.all()), 2)

    def test_user_profile(self):
        """Test profiles are connected to users."""
        assert self.profile_1.user == self.user_1
        assert self.profile_2.user == self.user_2

    def test_profile_route(self):
        """Test route are connected to profiles."""
        assert self.route_1.user == self.profile_1
        assert self.route_2.user == self.profile_2

    def test_profile_field(self):
        """Test required fields are provided."""
        self.assertNotEqual('a', self.profile_1.firstname)
        self.assertNotEqual('a', self.profile_1.lastname)
        self.assertNotEqual('a', self.profile_1.email)
        self.assertNotEqual('a', self.profile_1.phonenumber)
        self.assertNotEqual('a', self.profile_1.carbrand)
        self.assertNotEqual('a', self.profile_1.carseat)
        self.assertNotEqual('t', self.profile_1.petsallowed)


