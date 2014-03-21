from Products.CMFCore.utils import getToolByName
from zope.component.hooks import getSite
from zope.publisher.browser import BrowserView


class ImageSlider(BrowserView):
    """return list of images for slider
    """
    def __call__(self):
        catalog = getToolByName(self.context, 'portal_catalog')
        path = '/'.join(getSite().getPhysicalPath()) + '/sliderimages'
        return catalog({'portal_type': 'Image'}, path={'query': path})
