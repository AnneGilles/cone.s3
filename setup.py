from setuptools import setup, find_packages
import sys, os

version = '0.1dev'
shortdesc = 'cone.s3'
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(name='cone.s3',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Web Environment',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
            'License :: Free for non-commercial use',
      ],
      keywords='',
      author='BlueDynamics Alliance',
      author_email='dev@bluedynamics.com',
      url=u'',
      license='',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['cone'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'node.ext.ugm',
          'cone.app',
          'yafowil.yaml',
          'boto',
      ],
      extras_require = dict(
          test=[
                'interlude',
          ]
      ),
      tests_require=[
          'interlude',
      ],
      test_suite = "cone.s3.tests.test_suite",
      entry_points = """
      """
      )