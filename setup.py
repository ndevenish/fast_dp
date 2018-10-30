# in preparation for pypi packaging. We are not there yet

from __future__ import absolute_import, division, print_function

from setuptools import find_packages, setup

setup(name='fast_dp',
      description='fast_dp',
      url='https://github.com/DiamondLightSource/fast_dp',
      author='Markus Gerstel',
      author_email='scientificsoftware@diamond.ac.uk',
      download_url="https://github.com/DiamondLightSource/fast_dp/releases",
      version='0.1',
      install_requires=[],
      packages=find_packages(),
      license='Apache-2.0',
      entry_points={
        'libtbx.dispatcher': [
          'fast_dp=fast_dp',
          'fast_rdp=fast_rdp',
          'header2edna_xml=header2edna_xml',
        ],
      },
      scripts=[
        'bin/fast_dp',
        'bin/fast_rdp',
        'bin/header2edna_xml',
      ],
      tests_require=['mock', 'procrunner', 'pytest'],
      zip_safe=False,
      classifiers = [
        'Development Status :: 4 - Beta',
#       'License :: OSI Approved :: Apache Software License 2.0 (Apache-2.0)', # eventually. https://github.com/pypa/warehouse/issues/2996
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: POSIX :: Linux',
     ],
)