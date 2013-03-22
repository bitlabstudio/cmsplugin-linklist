"""Factories of the ``linklist`` app."""
import factory

from ..models import Link


class KairosLinkFactory(factory.Factory):
    FACTORY_FOR = Link

    title = 'Test Link'
    url = 'http://www.example.com'
