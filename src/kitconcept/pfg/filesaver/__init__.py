# -*- coding: utf-8 -*-
"""Init and utils."""

from zope.i18nmessageid import MessageFactory
import fileDataAdapter

from Products.Archetypes import atapi
from Products.CMFCore import utils
from Products.PloneFormGen.config import SDA_ADD_CONTENT_PERMISSION
from . import config

_ = MessageFactory('kitconcept.pfg.filesaver')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
    content_types, constructors, ftis = atapi.process_types(
        atapi.listTypes(config.PROJECTNAME),
        config.PROJECTNAME)
    for atype, constructor in zip(content_types, constructors):
        utils.ContentInit('%s: %s' % (config.PROJECTNAME, atype.portal_type),
            content_types=(atype,),
            permission=SDA_ADD_CONTENT_PERMISSION,
            extra_constructors=(constructor,),
).initialize(context)
