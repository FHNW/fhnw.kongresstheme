import os
from Globals import package_home
from Products.CMFCore.utils import getToolByName
from zope.annotation.interfaces import IAnnotations


def runCustomCode(site):
    """ These steps are only run on first installation
    """

    annotations = IAnnotations(site)
    if not 'kongresstheme-installed' in annotations:
        annotations['kongresstheme-installed'] = True

        """ cleanout not needed folders
        """
        if hasattr(site, 'news'):
            site.manage_delObjects(['news'])
        if hasattr(site, 'events'):
            site.manage_delObjects(['events'])
        if hasattr(site, 'Members'):
            site.manage_delObjects(['Members'])

        """ Import steps from the uploaded tarball.
        """
        fpath=os.path.join(package_home(globals()),'content/content.tgz')
        f = open(fpath, 'r')
        tarball = f.read()
        f.close()

        setup_tool = getToolByName(site, 'portal_setup')

        result = setup_tool.runAllImportStepsFromProfile(None, True, archive=tarball)

        steps_run = 'Steps run: %s' % ', '.join(result['steps'])

        return setup_tool.manage_importSteps(manage_tabs_message=steps_run,
                                       messages=result['messages'])


def setupVarious(context):
    """
    @param context: Products.GenericSetup.context.DirectoryImportContext instance
    """

    # We check from our GenericSetup context whether we are running
    # add-on installation for your product or any other proudct
    if context.readDataFile('fhnw.kongresstheme.marker.txt') is None:
        # Not your add-on
        return

    portal = context.getSite()

    runCustomCode(portal)
