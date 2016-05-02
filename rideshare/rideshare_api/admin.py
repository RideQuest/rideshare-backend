from django.contrib import admin
from rideshare_profile.models import Profile, Route

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    pass