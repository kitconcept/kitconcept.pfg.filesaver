""" A form action adapter that saves form submissions for download """
from .config import PROJECTNAME
from .interfaces import IFileDataAdapter
from AccessControl import ClassSecurityInfo
from plone.app.dexterity.interfaces import IDXFileFactory
from plone.dexterity.utils import createContentInContainer
from Products.Archetypes.public import *  # noqa
from Products.ATContentTypes.content.base import registerATCT
from Products.PloneFormGen.content.actionAdapter import FormActionAdapter
from Products.PloneFormGen.content.actionAdapter import FormAdapterSchema
from zope.contenttype import guess_content_type
from zope.interface import implements
from ZPublisher.HTTPRequest import FileUpload

import logging
import transaction


logger = logging.getLogger("PloneFormGen")


class FileDataAdapter(FormActionAdapter):
    """A form action adapter that will save form input data and
       return it in csv- or tab-delimited format."""
    implements(IFileDataAdapter)

    schema = FormAdapterSchema.copy()

    schema.moveField('execCondition', pos='bottom')

    meta_type = 'FileDataAdapter'
    portal_type = 'FileDataAdapter'
    archetype_name = 'File Data Adapter'

    immediate_view = 'fg_filedatasave_view'
    default_view = 'fg_filedatasave_view'

    security = ClassSecurityInfo()


    security.declarePrivate('onSuccess')  # noqa
    def onSuccess(self, fields, REQUEST=None, loopstop=False): # noqa
        # """
        # saves data.
        # """
        for f in fields:
            if f.isFileField():
                file_folder = self.get_file_folder()
                factory = IDXFileFactory(file_folder)
                file = REQUEST.form.get('%s_file' % f.fgField.getName())
                if isinstance(file, FileUpload) and file.filename != '':
                    file.seek(0)
                    fdata = file.read()
                    filename = file.filename
                    mimetype, enc = guess_content_type(filename, fdata, None)

                    factory(filename, mimetype, fdata)

    def get_file_folder(self):
        if not self.aq_parent.get('files', False):
            files_folder = createContentInContainer(
                self.aq_parent, 'Folder', checkConstraints=False, id='files',
                title='Saved Files')
            transaction.commit()
            return files_folder

        else:
            return self.aq_parent['files']


registerATCT(FileDataAdapter, PROJECTNAME)
