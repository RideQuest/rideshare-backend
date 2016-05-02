from django.contrib import admin
from rideshare_profile.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
