"""Models for the ``linklist`` app."""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from filer.fields.image import FilerImageField


class LinkCategory(models.Model):
    """
    Category for a link.

    """
    name = models.CharField(
        max_length=256,
        verbose_name=_('Name'),
    )

    def __unicode__(self):
        return self.name


class Link(models.Model):
    """
    Contains an URL and link-related data.

    :category: Optional category for this link
    :title: Title of the link.
    :url: URL of the link.
    :image: Screenshot of the link.
    :description: Long description of the link.
    :position: Current position integer of the object.
    :alignment: Choices to render the link left or right aligned.

    """
    category = models.ForeignKey(
        'LinkCategory',
        verbose_name=_('Link category'),
        related_name='links',
        null=True, blank=True,
    )

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

    alignment = models.CharField(
        verbose_name=_('Alignment'),
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


class LinklistCategoryPlugin(CMSPlugin):
    category = models.ForeignKey('LinkCategory', related_name='plugins')

    def __unicode__(self):
        return self.category.name
