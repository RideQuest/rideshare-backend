from django.contrib.auth.models import User
from rideshare_profile.models import Profile
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serialize user."""

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class ProfileSerializer(serializers.ModelSerializer):
    """Serialize user profile."""

    class Meta:
        model = Profile
        fields = ('firstname', 'lastname', 'email', 'phonenumber', 'carbrand', 'carseat', 'petsallowed')

