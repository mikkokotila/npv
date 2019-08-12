#! /usr/bin/env python

import os

DESCRIPTION = "Startup and Corporate Investment and Financial Planning Simulator for Python."
LONG_DESCRIPTION = """\
NPV provides a very high level simulation facility for getting the NPV
(net presevent value) score and other key metrics any business idea.
By default, the simulation automatically generates:

- monthly and annual income statement
- monthly and annual cashflow statement
- monthly and annual growth statistics

Simulation is based on set of input variables and volatility
computations that can be adjusted as needed for each project.

Additionally, facility for performing a Monte Carlo simulation is provided,
and a method for generating key financial metrics individually.

"""

DISTNAME = 'npv'
MAINTAINER = 'Mikko Kotila'
MAINTAINER_EMAIL = 'mailme@mikkokotila.com'
URL = 'http://github.com/mikkokotila'
LICENSE = 'MIT'
DOWNLOAD_URL = 'https://github.com/mikkokotila/npvpy'
VERSION = '0.4.1'

try:
    from setuptools import setup
    _has_setuptools = True
except ImportError:
    from distutils.core import setup


def check_dependencies():
    install_requires = ['wrangle', 'pandas', 'numpy', 'astetik']

    return install_requires


if __name__ == "__main__":

    install_requires = check_dependencies()

    setup(name=DISTNAME,
          author=MAINTAINER,
          author_email=MAINTAINER_EMAIL,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          long_description=LONG_DESCRIPTION,
          license=LICENSE,
          url=URL,
          version=VERSION,
          download_url=DOWNLOAD_URL,
          install_requires=install_requires,
          packages=['npv'],
          classifiers=[
                     'Intended Audience :: Science/Research',
                     'Programming Language :: Python :: 2.7',
                     'Programming Language :: Python :: 3.4',
                     'Programming Language :: Python :: 3.5',
                     'Programming Language :: Python :: 3.6',
                     'Operating System :: POSIX',
                     'Operating System :: Unix',
                     'Operating System :: MacOS'],
          )
