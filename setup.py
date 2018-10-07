#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(
    name='gridslice',
    version='1.0.0',
    description='Command line tool for slicing an image on a grid. Good for spritesheets and that kind of thing.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='jackw01',
    python_requires='>=3.3.0',
    url='https://github.com/jackw01/gridslice',
    packages=find_packages(),
    install_requires=[
        'Pillow>=5.3.0'
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'gridslice=gridslice:main'
        ]
    },
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)
