"""
PostgreSQL test settings for ``{{ app_name }}`` app.
"""

from {{ app_name }}.tests.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ app_name }}',
    }
}
