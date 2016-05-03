from django.apps import AppConfig


class RideshareApiConfig(AppConfig):
    name = 'rideshare_api'

    def ready(self):
        from rideshare_api import signals
