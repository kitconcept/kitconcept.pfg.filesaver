# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.interface import Interface


class IKitconceptPfgFilesaverLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IFileDataAdapter(Interface):
    ''' Interface for the ExampleContent type
    '''
