# from django.shortcuts import render
from rest_framework import generics
from serializers import UserSerializer
from django.contrib.auth.models import User


class UserEndpoint(generics.RetrieveUpdateDestroyAPIView):
    """Endpoint for user model."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permisions here
