"""
App configuration for ``{{ app_name }}`` app.
"""

# Register signal handlers, but avoid interacting with the database.
# See: https://docs.djangoproject.com/en/1.8/ref/applications/#django.apps.AppConfig.ready

from django.apps import AppConfig


class AppConfig(AppConfig):
    name = '{{ app_name }}'
    # verbose_name = '{{ app_name }}'

    def ready(self):
        pass
