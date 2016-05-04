"""Test User, Profile and model."""
from django.test import TestCase, Client
from .models import Profile, Route
from django.contrib.auth.models import User

class TestProfile(TestCase):
    """Test profile functionality."""

    def setUp(self):
        """Test new user creation."""
        self.client = Client()

        self.test1 = User.objects.create_user('driver1')
        self.test2 = User.objects.create_user('rider1')
        self.test1.save()
        self.test2.save()

        self.user3 = User.objects.create_user(username='Dear Test', password='pycov')
        self.user = self.client.login(username='Dear Test', password='pycov')

    def test_verify_save(self):
        """Test user saved ."""
        self.assertEquals(len(User.objects.all()), 3)



