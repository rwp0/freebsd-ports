#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['flit_scm']

package_data = \
{'': ['*']}

install_requires = \
['flit-core~=3.5', 'setuptools_scm~=6.4', 'tomli']

setup(name='flit_scm',
      version='%%PORTVERSION%%',
      description='A PEP 518 build backend that uses setuptools_scm to generate a version file from your version control system, then flit to build the package.',
      author=None,
      author_email='Will Da Silva <will@willdasilva.xyz>',
      url=None,
      packages=packages,
      package_data=package_data,
      install_requires=install_requires,
      python_requires='>=3.6',
     )
