from django.conf.urls import url, include
from rideshare_api import views


urlpatterns = [
    # url(r'^users/', views.UserEndpoint.as_view(), name='user_endpoint'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserEndpoint.as_view(),
        name='user_endpoint'),
    url(r'^profiles/(?P<pk>[0-9]+)/$', views.ProfileEndpoint.as_view(),
        name='profile_endpoint'),
]
