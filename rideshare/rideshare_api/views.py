# from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, ProfileSerializer, RouteSerializer
from django.contrib.auth.models import User
from rideshare_profile.models import Profile, Route
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from django.contrib.gis.measure import D
from django.contrib.gis import geos
from django.core.serializers import serialize


class ModifyUserEndpoint(generics.RetrieveUpdateDestroyAPIView):
    """Endpoint for modifying a user."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated)
    authentication_classes = (BasicAuthentication, TokenAuthentication)


class CreateUserEndpoint(generics.ListCreateAPIView):
    """Endpoint for creating a user."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileEndpoint(generics.RetrieveUpdateDestroyAPIView):
    """Endpoint for profile model."""

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BasicAuthentication, TokenAuthentication)


class RouteEndpoint(generics.RetrieveUpdateDestroyAPIView):
    """Endpoint for profile model."""

    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BasicAuthentication, TokenAuthentication)


class RouteCreateEndpoint(generics.ListCreateAPIView):
    """Endpoint for profile model."""

    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BasicAuthentication, TokenAuthentication)


class RouteQueryEndpoint(generics.ListCreateAPIView):
    """Endpoint for query."""
    serializer_class = RouteSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BasicAuthentication, TokenAuthentication)

    def get_queryset(self):
        request = self.request
        lat = request.GET['lat']
        lng = request.GET['lng']
        point = geos.Point(float(lat), float(lng))
        result = Route.objects.filter(start_point__distance_lt=(point, D(m=50)))
        return result



