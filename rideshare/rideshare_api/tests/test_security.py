from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
import factory
from rideshare_profile.models import Profile, Route


class ProfileFactory(factory.django.DjangoModelFactory):
    """Profile factory."""

    class Meta:
        model = Profile


class RouteFactory(factory.django.DjangoModelFactory):
    """Route factory."""

    class Meta:
        model = Route


class UnAuthSecurityTests(APITestCase):
    """Test Security without auth."""

    def test_access_user(self):
        """Test unauth access to users."""
        c = APIClient()
        response = c.post('/users/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_access_specific_user(self):
        """Test unauth access to users."""
        c = APIClient()
        response = c.post('/users/1')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_access_route_add(self):
        """Test unauth access to routes add."""
        c = APIClient()
        response = c.post('/routes/add')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_access_route(self):
        """Test unauth access to all routes."""
        c = APIClient()
        response = c.post('/routes/1')
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

    def test_access_profile(self):
        """Test unauth access to profile information."""
        c = APIClient()
        response = c.post('/profiles/1')
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)


class AuthSecurityTest(APITestCase):
    """Test routes with authentication."""

    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = User.objects.create_user('MJTestorus',
                                             email='test@test.com',
                                             password='test')
        self.user.save()

        self.Profile = ProfileFactory.create(
            user=self.user,
            firstname='Spud',
            lastname='Williams',
            email='test@test.com',
            carbrand='Toyota',
            carseat=4,
            petsallowed=True,
        )
        self.Profile.save()

        token = Token.objects.get(user__username='MJTestorus')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_authentic_profile(self):
        """Test auth access to profiles."""
        response = self.client.get('/profiles/{}/'.format(self.user.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authentic_user(self):
        """Test auth access to users."""
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
