# -*- coding: utf-8 -*-
import setuptools
import re
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

def version_url():
    with open(os.path.join('./doifrombibtex', '__init__.py')) as f:
        for line in f:
            if line.startswith('__version__'):
                v = line.replace("'", '').split()[-1]
            if line.startswith('__url__'):
                url = line.replace('"', '').split()[-1]
                return v, url


version, url = version_url()

setuptools.setup(
    name="doifrombibtex",
    version=version,
    author="B. Nennig",
    author_email="benoit.nennig@supmeca.fr",
    description="An utility to parse bibtex files in order to recover the missing DOI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=url,
    packages=['doifrombibtex'],
    package_data={'doifrombibtex': ['examples/*.bib']},
    scripts=['bin/doifrombibtex'],
    install_requires=['bibtexparser',
                      'crossrefapi'],  # max version for python3.5
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: GPL 3",
        "Operating System :: OS Independent",
    ],
    # tested with python 3.5 may works with previous py3 version...
    python_requires='>=3.5',
)
