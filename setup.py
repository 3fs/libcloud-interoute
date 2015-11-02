#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='libcloud-interoute',
    version='0.0.1',
    description='Apache Libcloud driver for Interoute',
    author='3fs',
    url='https://github.com/3fs/libcloud-interoute',
    download_url='https://github.com/3fs/libcloud-interoute/releases/tag/0.0.1',
    packages=[
        'interoute',
        'interoute.libcloud'
    ],
    install_requires=[
        'apache-libcloud>=0.18.0'
    ],
    zip_safe=False,
    license='Apache License 2.0',
)
