from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from rideshare_profile.models import Profile, Route
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate
from rest_framework import status

from rideshare_api.views import (ModifyUserEndpoint,
                                 CreateUserEndpoint,
                                 ProfileEndpoint,
                                 RouteEndpoint,
                                 RouteCreateEndpoint,
                                 )

from django.contrib.gis.geos import GEOSGeometry
# from myproject.apps.core.models import Account
# not sure how to configure the above import


class TestEndpoints(APITestCase):
    """Test request and response of endpoints."""

    def setUp(self):
        """Setup."""
        self.client = APIClient()
        self.profile = Profile()
        self.user = User.objects.create_user(username='foo', password='foobared')

        self.client.force_authenticate(user=self.user)
        self.profile.user = self.user
        self.profile.carbrand = 'Audi'
        self.profile.carseat = 1
        self.profile.petsallowed = True
        self.profile.save()
        self.route = Route()
        self.route.user = self.profile
        self.route.start_point = GEOSGeometry('POINT(2 3)', srid=4326)
        self.route.save()

    def tearDown(self):
        """Teardown."""
        User.objects.all().delete()
        Profile.objects.all().delete()
        Route.objects.all().delete()

    # def test_post_user

    def test_get_user(self):
        """Test that a user returned when a get request is performed."""
        response = self.client.get('/users/{}/').format(self.user.id)
        self.assertEqual(response.data[0]['username'], 'foo')

    # def test_post_user(self):
    #     """Test that a user is created when a post request is performed."""
    #     post = self.client.post('/users/', {'username': 'joe',
    #                                         'password': 'i love beer'})
    #     self.assertEquals(post.data['username'], 'joe')
    #     self.assertEquals(post.data['password'], 'i love beer')

    # def test_get_route(self):
    #     """Test that you can get a route."""
    #     # this test is passing but presents a problem that if moved 
    #     # the test pk will fail with a KeyError
    #     response = self.client.get('/routes/2/')
    #     self.assertEqual(response.data['start_point'],
    #                      u'SRID=4326;POINT (2.0000000000000000 3.0000000000000000)')

    # def test_get_route_no_route_exists(self):
    #     """Test that you can get a route."""
    #     response = self.client.get('/routes/1/')
    #     self.assertEqual(response.data, {u'detail': u'Not found.'})

    # def test_get_profile(self):
    #     """Test that you can get a profile."""
    #     response = self.client.get('/profiles/1/')
    #     self.assertEqual(response.data['carbrand'], 'Audi')

    # def test_add_route(self):
    #     """Test that a post to /routes/add/ behaves as expected."""
    #     post = self.client.post('/routes/add/', {'user': 1,
    #                                              'start_point': u'SRID=4326;POINT (2.0000000000000000 3.0000000000000000)'})
    #     get = self.client.get('/routes/1/')
    #     self.assertEquals(get.data['user'], 1)
  


# class ModifyUserEndpoint(generics.RetrieveUpdateDestroyAPIView):
#     """Endpoint for modifying a user."""

#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsAuthenticated)
#     authentication_classes = (BasicAuthentication, TokenAuthentication)


# class CreateUserEndpoint(generics.ListCreateAPIView):
#     """Endpoint for creating a user."""

#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class ProfileEndpoint(generics.RetrieveUpdateDestroyAPIView):
#     """Endpoint for profile model."""

#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = (IsAuthenticated,)
#     authentication_classes = (BasicAuthentication, TokenAuthentication)


# class RouteEndpoint(generics.RetrieveUpdateDestroyAPIView):
#     """Endpoint for profile model."""

#     queryset = Route.objects.all()
#     serializer_class = RouteSerializer
#     permission_classes = (IsAuthenticated,)
#     authentication_classes = (BasicAuthentication, TokenAuthentication)


# class RouteCreateEndpoint(generics.ListCreateAPIView):
#     """Endpoint for profile model."""

#     queryset = Route.objects.all()
#     serializer_class = RouteSerializer
#     permission_classes = (IsAuthenticated,)
#     authentication_classes = (BasicAuthentication, TokenAuthentication)

