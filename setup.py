#!/usr/bin/env python

from setuptools import setup

setup(name='application',
      version='0.1',
      description='A Flask application',
      author='Author Name',
      author_email='author@example.com',
      url='example.com',
      packages=[
          'application'
      ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'Flask',
          'Flask-Migrate',
          'Flask-Script',
          'Flask-SQLAlchemy',
          'Flask-WTF',
      ],
      scripts=['manage.py'])
