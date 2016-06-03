from django.contrib.auth.models import User
from rideshare_profile.models import Profile, Route
from rest_framework import serializers
from django.core.serializers import serialize
from django.contrib.gis import geos


class UserSerializer(serializers.ModelSerializer):
    """Serialize user."""

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password',)


class ProfileSerializer(serializers.ModelSerializer):
    """Serialize user profile."""

    class Meta:
        model = Profile
        fields = ('id', 'user', 'firstname', 'lastname', 'email', 'phonenumber',
                  'carbrand', 'carseat', 'petsallowed')


class RouteSerializer(serializers.ModelSerializer):
    """Serialize route."""

    class Meta:
        model = Route
        fields = ('id', 'user', 'start_point')
