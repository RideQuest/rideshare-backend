from django.conf.urls import url, include
from rideshare_api import views


urlpatterns = [
    url(r'^profiles/(?P<pk>[0-9]+)/$', views.ProfileEndpoint.as_view(),
        name='profile_endpoint'),
    url(r'^profiles/add', views.ProfileCreateEndpoint.as_view(),
        name='profile_create_endpoint'),
    url(r'^routes/(?P<pk>[0-9]+)/$', views.RouteEndpoint.as_view(),
        name='route_endpoint'),
    url(r'^routes/add', views.RouteCreateEndpoint.as_view(),
        name='route_add'),
    url(r'^users/signup', views.CreateUserEndpoint.as_view(),
        name='create_user_endpoint'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.ModifyUserEndpoint.as_view(),
        name='modify_user_endpoint'),
    url(r'^query/', views.RouteQueryEndpoint.as_view()),
    url(r'^auth-token/', views.ObtainAuthToken.as_view()),
    url(r'^avatar/', views.AddAvatarEndpoint.as_view(),
        name='create_avatar_endpoint'),
    url(r'^avatar/(?P<pk>[0-9]+)/$', views.UpdateAvatarEndpoint.as_view(),
        name='modify_user_endpoint'),
]
