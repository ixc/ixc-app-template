"""
Admin configuration for ``{{ app_name }}`` app.
"""

# Define `list_display`, `list_filter` and `search_fields` for each model.
# These go a long way to making the admin more usable.

from django.contrib import admin

from {{ app_name }} import models
