#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2017, OneLogin, Inc.
# All rights reserved.

from setuptools import setup


version = {}
with open("src/onelogin/api/version.py") as fp:
    exec(fp.read(), version)

setup(
    name='onelogin',
    version=version['__version__'],
    description="OneLogin Python SDK. Use this API client to interact with OneLogin's platform",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    author='OneLogin',
    author_email='support@onelogin.com',
    license='MIT',
    url='https://github.com/onelogin/onelogin-python-sdk',
    packages=[
        'onelogin',
        'onelogin/api',
        'onelogin/api/util',
        'onelogin/api/models'
    ],
    package_dir={
        '': 'src',
    },
    install_requires=[
        'requests>=2,<3',
        'defusedxml>=0.5',
        'python-dateutil>=2,<3'
    ],
    test_suite='tests',
    extras_require={
        'test': (
            'coverage>=3,<6',
            'pylint>=1,<3',
            'pep8>=1,<2',
            'pyflakes>=1,<3',
        ),
    },
    keywords='onelogin api sdk',)
