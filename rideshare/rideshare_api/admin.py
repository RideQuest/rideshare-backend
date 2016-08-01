from django.contrib import admin
from rideshare_profile.models import Profile, Route, Avatar

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    pass

@admin.register(Avatar)
class AvatarAdmin(admin.ModelAdmin):
    pass
