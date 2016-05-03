from django.contrib.auth.models import User
from rideshare_profile.models import Profile, Route
from rest_framework import serializers
from django.core.serializers import serialize


class UserSerializer(serializers.ModelSerializer):
    """Serialize user."""

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password',)


class ProfileSerializer(serializers.ModelSerializer):
    """Serialize user profile."""

    class Meta:
        model = Profile
        fields = ('id', 'first_name', 'last_name', 'email', 'phone_number',
                  'car_brand', 'car_seat', 'pets_allowed')


class RouteSerializer(serializers.ModelSerializer):
    """Serialize route."""

    class Meta:
        model = Route
        fields = ('id', 'in_profile', 'point')
