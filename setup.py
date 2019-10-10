#!/usr/bin/env python

from setuptools import setup

setup(name='TakeTheTime',
      version='0.3',
      description='Take The Time, a time-taking library for Python',
      author='Erik Bjäreholt',
      author_email='erik@bjareho.lt',
      url='https://github.com/ErikBjare/TakeTheTime',
      packages=['takethetime'],
      install_requires=[
          'typing'
      ])
