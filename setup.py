#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name="sandsnake",
    license='Apache License 2.0',
    version="0.1.0ALPHA",
    description="Manage activity indexes for objects.",
    long_description=open('README.rst', 'r').read(),
    author="Numan Sachwani",
    author_email="numan856@gmail.com",
    url="https://github.com/numan/sandsnake",
    packages=find_packages(exclude=['tests']),
    test_suite='nose.collector',
    install_requires=[
        'nydus==0.10.3',
        'redis==2.7.2',
        'hiredis==0.1.1',
        'python-dateutil==1.5',
    ],
    tests_require=[
        'nose>=1.0',
    ],
    classifiers=[
        "Intended Audience :: Developers",
        'Intended Audience :: System Administrators',
        "Programming Language :: Python",
        "Topic :: Software Development",
        "Topic :: Utilities",
    ],
)
