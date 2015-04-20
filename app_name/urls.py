"""
URLconf for ``{{ app_name }}`` app.
"""

# Prefix URL names with the app name. Avoid URL namespaces unless it is likely
# this app will be installed multiple times in a single project.

from django.conf.urls import include, patterns, url

urlpatterns = patterns(
    '{{ app_name }}.views',
    url(r'^$', 'index', name='{{ app_name }}_index'),
)
