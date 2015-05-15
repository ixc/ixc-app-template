"""
Root URLconf for ``{{ app_name }}.tests`` project.
"""

from django.conf.urls import include, patterns, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^{{ app_name }}/', include('{{ app_name }}.urls')),
)
