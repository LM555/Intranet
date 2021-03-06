#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(name='intranet',
    version='0.1',
    description="",
    long_description="""""",
    keywords='',
    author='',
    author_email='info@kiberpipa.org',
    url='http://www.kiberpipa.org',
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    packages=find_packages(),
    classifiers=[
    ],
    install_requires=[
        # deprecated
        'BeautifulSoup',
        'simplejson',  # TODO: use json
        # other
        'reportlab',
        'PyExcelerator',
        'html2text',
        'pytz',
        'pygments',
        # intranet.org
        'python-ldap',
        # intranet.www
        'python-memcached',
        'flickrapi',
        'requests',
        'python-dateutil',
        'django-mailman',
        # django stuff
        'Django>=1.4',
        'Feedjack',
        'django-tagging',
        'Pillow',  # properly distributed PIL
        'South',
        'django-honeypot',
        'django-grappelli',
        'django-gravatar2',
        'django-chosen',
        # development
        'django-debug-toolbar',
        'django-extensions',
        'Werkzeug',  # interactive debug
        'django-coverage',
        'coverage',
        'django-tinymce',
        # solr
        'django-haystack',
        'pysolr',
        # database
        'psycopg2',
        'egenix-mx-base',
        # commands
        'twitter',
        # admin
        'raven',
        'django-reversion',
    ],
    tests_require=[
        'nose',
    ],
)
