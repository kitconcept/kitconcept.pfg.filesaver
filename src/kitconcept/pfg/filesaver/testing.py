# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import kitconcept.pfg.filesaver


class KitconceptPfgFilesaverLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=kitconcept.pfg.filesaver)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'kitconcept.pfg.filesaver:default')


KITCONCEPT_PFG_FILESAVER_FIXTURE = KitconceptPfgFilesaverLayer()


KITCONCEPT_PFG_FILESAVER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(KITCONCEPT_PFG_FILESAVER_FIXTURE,),
    name='KitconceptPfgFilesaverLayer:IntegrationTesting'
)


KITCONCEPT_PFG_FILESAVER_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(KITCONCEPT_PFG_FILESAVER_FIXTURE,),
    name='KitconceptPfgFilesaverLayer:FunctionalTesting'
)


KITCONCEPT_PFG_FILESAVER_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        KITCONCEPT_PFG_FILESAVER_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='KitconceptPfgFilesaverLayer:AcceptanceTesting'
)
