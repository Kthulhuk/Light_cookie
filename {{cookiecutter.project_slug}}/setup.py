#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = ['docopt', 'sphinx', 'autodoc', 'coverage',
                'flake8', 'chardet']  # TODO: put package requirements here

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'GNU Lesser General Public License v3': 'License :: OSI Approved :: GNU Lesser General Public License v3',
    'GNU Affero General Public License v3': 'License :: OSI Approved :: GNU Affero General Public License v3',
} %}

setup(
    name='{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.version }}',
    description="{{ cookiecutter.project_short_description }}",
    url='https://github.com/Kthulhuk/{{ cookiecutter.project_name | replace(" ", "_") }}',
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    packages=find_packages(include=['{{ cookiecutter.project_slug }}']),
    include_package_data=True,
    install_requires=requirements,
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    keywords='{{ cookiecutter.project_slug }}',
    classifiers=[
{%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
)
