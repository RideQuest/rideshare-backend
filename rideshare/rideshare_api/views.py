# from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, ProfileSerializer, RouteSerializer
from django.contrib.auth.models import User
from rideshare_profile.models import Profile, Route
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token
from django.utils.translation import ugettext_lazy as _
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import parsers, renderers
from django.utils.six import text_type
import base64
import binascii
from rest_framework import HTTP_HEADER_ENCODING, exceptions


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser,
                      parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != b'basic':
            return None

        if len(auth) == 1:
            msg = _('Invalid basic header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)

        elif len(auth) > 2:
            msg = _('Invalid basic header. Credentials string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            auth_parts = base64.b64decode(auth[1]).decode(HTTP_HEADER_ENCODING).partition(':')

        except (TypeError, UnicodeDecodeError, binascii.Error):
            msg = _('Invalid basic header. Credentials not correctly base64 encoded.')
            raise exceptions.AuthenticationFailed(msg)

        userid, password = auth_parts[0], auth_parts[2]

        credentials = {
            'username': userid,
            'password': password
        }
        user = authenticate(**credentials)
        if user is None:
            raise exceptions.AuthenticationFailed(_('Invalid username/password.'))

        if not user.is_active:
            raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))

        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


def get_authorization_header(request):
    auth = request.META.get('HTTP_AUTHORIZATION', b'')
    if isinstance(auth, text_type):
        auth = auth.encode(HTTP_HEADER_ENCODING)
    return auth


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
