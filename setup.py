#!/usr/bin/env python
from distutils.core import setup

setup(
    name='django-qsstats-magic',
    version='0.5.2',
    description='A django microframework that eases the generation of aggregate data for querysets.',
    long_description = open('README.rst').read(),
    author='Matt Croydon, Mikhail Korobov',
    author_email='mcroydon@gmail.com, kmike84@gmail.com',
    url='http://bitbucket.org/kmike/django-qsstats-magic/',
    packages=['qsstats'],
    requires=['dateutil(>=1.4.1, < 2.0)']
)
