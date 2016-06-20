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

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


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
