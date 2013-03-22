"""Models for the ``linklist`` app."""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from filer.fields.image import FilerImageField


class Link(models.Model):
    """
    Contains an URL and link-related data.

    :title: Title of the link.
    :url: URL of the link.
    :image: Screenshot of the link.
    :description: Long description of the link.
    :order: Choices to render the link left or right aligned.

    """
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=50,
    )

    url = models.URLField(
        verbose_name=_('URL'),
        max_length=50,
    )

    image = FilerImageField(
        verbose_name=_('Image'),
        related_name='link_images',
    )

    description = models.TextField(
        verbose_name=_('Description'),
        max_length=500,
        blank=True,
    )

    position = models.PositiveIntegerField(
        verbose_name=_('Position'),
        blank=True, null=True,
    )

    order = models.CharField(
        verbose_name=_('Order'),
        max_length=10,
        choices=(
            ('left', 'left'),
            ('right', 'right'),
        ),
    )

    class Meta:
        ordering = ['position']

    def __unicode__(self):
        return '{0}'.format(self.title)
