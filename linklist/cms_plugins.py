"""django-cms plugins for the ``linklist`` app."""
from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import Link


class CMSLinkPlugin(CMSPluginBase):
    name = _('Linklist')
    render_template = "linklist/link_list.html"

    def render(self, context, instance, placeholder):
        context.update({
            'object_list_left': Link.objects.filter(order='left'),
            'object_list_right': Link.objects.filter(order='right'),
            'placeholder': placeholder,
        })
        return context


plugin_pool.register_plugin(CMSLinkPlugin)
