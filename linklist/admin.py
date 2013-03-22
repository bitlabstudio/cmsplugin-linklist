"""Admin objects for the ``linklist`` app."""
from django.contrib import admin

from .models import Link


class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'position')
    list_editable = ('position', )


admin.site.register(Link, LinkAdmin)
