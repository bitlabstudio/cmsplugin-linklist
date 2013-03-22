"""Tests for the models of the ``linklist`` app."""
from django.test import TestCase

from ..models import Link


class KairosLinkTestCase(TestCase):
    """Tests for the ``Link`` model class."""
    longMessage = True

    def test_instantiation(self):
        """Test if the ``Link`` model instantiates."""
        link = Link()
        self.assertTrue(link, msg='Should be correctly instantiated.')
