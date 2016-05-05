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


class AllAccess(APITestCase):
    """Test urls that do not have protection."""

    def test_access_registration(self):
        """Test  access to registration."""
        c = APIClient()
        response = c.get('/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_access_specific_user(self):
        """Test unauth access to registration."""
        c = APIClient()
        response = c.get('/users/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UnAuthSecurityTests(APITestCase):
    """Test Security without auth."""

    def setUp(self):
        """Setup with user."""
        self.other = User.objects.create_user('OTHER',
                                              email='test@test.com',
                                              password='test')
        self.other.save()
        self.OtherProfile = ProfileFactory.create(
            user=self.other,
            firstname='Mystery',
            lastname='Person',
            email='test@test.com',
            carbrand='Buick',
            carseat=4,
            petsallowed=True,
        )
        self.OtherProfile.save()

    def test_access_route_add(self):
        """Test unauth access to routes add."""
        c = APIClient()
        response = c.post('/routes/add')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_access_profile(self):
        """Test unauth access to profile information."""
        c = APIClient()
        response = c.post('/profiles/{}/'.format(self.other.pk))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_access_route(self):
        """Test unauth access to all routes."""
        c = APIClient()
        response = c.post('/routes/{}/'.format(self.other.pk))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_access_routequery(self):
        """Test unauth access to route query url."""
        c = APIClient()
        response = c.post('/query/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class AuthSecurityTest(APITestCase):
    """Test routes with authentication."""

    def setUp(self):
        """Setup."""
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = User.objects.create_user('MJTestorus',
                                             email='test@test.com',
                                             password='test')
        self.user.save()
        self.profile = ProfileFactory.create(
            user=self.user,
            firstname='Spud',
            lastname='Williams',
            email='test@test.com',
            carbrand='Toyota',
            carseat=4,
            petsallowed=True,
        )
        self.profile.save()
        self.route = RouteFactory.create(
            user=self.profile,
            start_point="SRID=4326;POINT (2.0000000000000000 3.0000000000000000)"
        )
        self.route.save()

        self.other = User.objects.create_user('OTHER',
                                              email='test@test.com',
                                              password='test')
        self.other.save()
        self.otherprofile = ProfileFactory.create(
            user=self.other,
            firstname='Mystery',
            lastname='Person',
            email='test@test.com',
            carbrand='Buick',
            carseat=4,
            petsallowed=True,
        )
        self.otherprofile.save()
        self.otherroute = RouteFactory.create(
            user=self.otherprofile,
            start_point="SRID=4326;POINT (2.0000000000000000 3.0000000000000000)"
        )
        self.otherroute.save()

        token = Token.objects.get(user__username='MJTestorus')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_authentic_profile(self):
        """Test auth access to profiles."""
        response = self.client.get('/profiles/{}/'.format(self.user.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authentic_other_profiles(self):
        """Test auth for viewing other profiles."""
        response = self.client.get('/profiles/{}/'.format(self.other.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authentic_routes(self):
        """Test auth access to routes."""
        response = self.client.get('/routes/{}/'.format(self.user.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authentic_other_routes(self):
        """Test auth for viewing other routes."""
        response = self.client.get('/routes/{}/'.format(self.other.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authentic_query(self):
        """Test auth access to search routes."""
        response = self.client.get('/query/',
                                   {'lat': '2.0000000000000001',
                                    'lng': '3.0000000000000002'}
                                   )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
