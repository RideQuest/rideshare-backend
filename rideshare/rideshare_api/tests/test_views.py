from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
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
# from myproject.apps.core.models import Account
# not sure how to configure the above import


class TestEndpoints(APITestCase):
    """Test request and response of endpoints."""

    def setUp(self):
        """Setup."""
        self.client = APIClient()
        self.user = User.objects.create_user(username='foo', password='foobared')
        self.client.force_authenticate(user=self.user)

    def test_get_user(self):
        """Test that a user is created when posted to user endpoint."""
        response = self.client.get('/users/1/')
        self.assertEqual(response.data[0]['username'], 'foo')

    def test_get_route(self):
        """Test that you can get a route."""
        response = self.client.get('path')


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
