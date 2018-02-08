# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from kitconcept.pfg.filesaver.testing import KITCONCEPT_PFG_FILESAVER_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that kitconcept.pfg.filesaver is properly installed."""

    layer = KITCONCEPT_PFG_FILESAVER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if kitconcept.pfg.filesaver is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'kitconcept.pfg.filesaver'))

    def test_browserlayer(self):
        """Test that IKitconceptPfgFilesaverLayer is registered."""
        from kitconcept.pfg.filesaver.interfaces import (
            IKitconceptPfgFilesaverLayer)
        from plone.browserlayer import utils
        self.assertIn(IKitconceptPfgFilesaverLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = KITCONCEPT_PFG_FILESAVER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['kitconcept.pfg.filesaver'])

    def test_product_uninstalled(self):
        """Test if kitconcept.pfg.filesaver is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'kitconcept.pfg.filesaver'))

    def test_browserlayer_removed(self):
        """Test that IKitconceptPfgFilesaverLayer is removed."""
        from kitconcept.pfg.filesaver.interfaces import IKitconceptPfgFilesaverLayer
        from plone.browserlayer import utils
        self.assertNotIn(IKitconceptPfgFilesaverLayer, utils.registered_layers())
