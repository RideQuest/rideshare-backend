# from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer, ProfileSerializer
from django.contrib.auth.models import User
from rideshare_profile.models import Profile


class UserEndpoint(generics.RetrieveUpdateDestroyAPIView):
    """Endpoint for user model."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permisions here


class ProfileEndpoint(generics.RetrieveUpdateDestroyAPIView):
    """Endpoint for profile model."""

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
