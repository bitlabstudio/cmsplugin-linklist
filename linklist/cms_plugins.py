"""django-cms plugins for the ``linklist`` app."""
from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import Link, LinklistCategoryPlugin


class CMSLinkPlugin(CMSPluginBase):
    name = _('Linklist')
    render_template = "linklist/link_list.html"

    def render(self, context, instance, placeholder):
        context.update({
            'object_list_left': Link.objects.filter(alignment='left'),
            'object_list_right': Link.objects.filter(alignment='right'),
            'placeholder': placeholder,
        })
        return context


class CMSLinklistCategoryPlugin(CMSPluginBase):
    model = LinklistCategoryPlugin
    name = _("Linklist Category Plugin")
    render_template = "linklist/category_list.html"

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'object_list': instance.category.links.all(),
        })
        return context


plugin_pool.register_plugin(CMSLinkPlugin)
plugin_pool.register_plugin(CMSLinklistCategoryPlugin)
