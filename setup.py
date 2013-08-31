#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages
from pyrate import __version__


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Communications',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Programming Language :: Python',
]

setup(
    name='pyrate',
    version=__version__,
    description='Pyrate is a python wrapper for restful web apis. It\'s like magic but simpler.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author='Kim Thoenen',
    author_email='kim@smuzey.ch',
    url='https://github.com/chive/pyrate',
    packages=find_packages(),
    license='MIT',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    include_package_data=True,
    zip_safe=False,

    install_requires=[
        open("requirements.txt").readlines(),
    ],
    entry_points={
        'console_scripts': [
            'pyratetools = pyrate.scripts.cliutils:main',
        ]
    },)