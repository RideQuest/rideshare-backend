from django.conf.urls import url, include
from rideshare_api import views
from rest_framework.authtoken.models import views as authviews


urlpatterns = [
    url(r'^profiles/(?P<pk>[0-9]+)/$', views.ProfileEndpoint.as_view(),
        name='profile_endpoint'),
    url(r'^users/', views.CreateUserEndpoint.as_view(), name='create_user_endpoint'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.ModifyUserEndpoint.as_view(),
        name='modify_user_endpoint'),
    url(r'^auth-token/', authviews.obtain_auth_token)
]
