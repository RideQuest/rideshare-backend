from django.core.urlresolvers import reverse
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

    # def setUp(self):
    #     """Setup."""
    #     factory = APIRequestFactory(enforce_csrf_checks=True)
        # get_request = 
        # self.post_request = factory.post('/users/', {'username': 'foo',
        #                                              'password': 'foobared'})
        # self.get_request = factory.get('/users/', {'username': 'foo',
        #                                            'password': 'foobared'})

    def test_user_created(self):
        """Test that a user is created when posted to user endpoint."""
        # import pdb; pdb.set_trace()
        factory = APIRequestFactory(enforce_csrf_checks=True)
        post = factory.post("/users/", {"username": "foo",
                            "password": "foobared"})
        self.assertEqual(post.body, '{"username":"foo","password":"foobared"}')

    def test_user_created(self):
        """Test that a user is created when posted to user endpoint."""
        client = APIClient()
        response = client.get('/users/1/')
        factory = APIRequestFactory(enforce_csrf_checks=True)
        post = factory.post("/users/", {"username": "foo",
                            "password": "foobared"})

        get = factory.get("/users/1/")
        self.assertEqual(get.body, '{"username":"foo","password":"foobared"}')


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
