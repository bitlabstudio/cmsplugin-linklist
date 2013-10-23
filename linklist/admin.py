"""Admin objects for the ``linklist`` app."""
from django.contrib import admin

from . import models


class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'position')
    list_editable = ('position', )


admin.site.register(models.Link, LinkAdmin)
admin.site.register(models.LinkCategory)
