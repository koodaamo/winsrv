from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(name='sidekick',
      version=version,
      description="On-premises server sidekick",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Petri Savolainen',
      author_email='petri.savolainen@koodaamo.fi',
      url='',
      license='Proprietary',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
