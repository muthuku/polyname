#!/usr/bin/env python
import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.1.0'
PACKAGE_NAME = 'polyname'
AUTHOR = 'Pragati Muthukumar'
AUTHOR_EMAIL = 'pragati.muthukumar@nrel.gov'
URL = 'https://github.com/muthuku/polyname'

LICENSE = 'MIT License'
DESCRIPTION = 'Extract polymer names and get monomer names and smile strings using existing database, Pubchem or CIRPY'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'numpy',
      'pandas',
      'itertools',
      'csv'
      'pubchempy'
      'cirpy'
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )
