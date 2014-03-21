from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='fhnw.kongresstheme',
      version=version,
      description="Diazo based Theme Package for FHNW Kongress Websites",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='Plone, Theme, Diazo',
      author='Peter Holzer',
      author_email='peter.holzer@agitator.com',
      url='http://www.agitator.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['fhnw'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'z3c.jbot',
          'webcouturier.dropdownmenu',
          'quintagroup.transmogrifier',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
