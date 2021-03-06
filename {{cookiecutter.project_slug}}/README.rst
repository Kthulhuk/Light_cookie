{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

Overview
--------

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.project_slug | replace(" ", "_") }}.readthedocs.io.
{% endif %}

Installation
------------

To install use pip:

    $ pip3 install {{ cookiecutter.project_slug }}


Or clone the repo:

    $ git clone http://gitlab.lan/C3NRD/{{ cookiecutter.project_slug }}

    $ python3 setup.py install
    

Usage
-----

Documentation
=============

Read the documentation to understand how to use {{ cookiecutter.project_name }}.

Helper targets
==============

To build the documentation, run:

    $ make doc
    
To run the test, run :

    $ make test

To check the code's superficial cleanliness run:

    $ make lint
    
To run tests each time a Python file is edited

    $ make live

Dev cycle
=========

One branch derived from latest master per new feature or bug fix.

When this branch is complete:

- Merge master back in it
        
        $ git merge master
        
- Make sure all tests pass, the code is clean and the doc compiles:

        $ make
        
- Bump the version appropriately (no tags):

        $ bumpversion (major|minor|patch) --commit --no-tag
        
- Rebase everything in order to make one commit (if more are needed, talk the the maintainer). To avoid catastrophic failure, create another branch that won't be rebased first. Keep bumpversion's commit message somewhere in the rebased commit message, but not always on the first line.

        $ git branch <my_feature>_no_rebase
        $ git rebase -i master
        
- Make a pull request, or, if you are the maintainer, switch to master

        $ git checkout master
        
- If you are the maintainer, merge the feature branch:
        
        $ git merge <my_feature>
        
- If you are the maintainer, make sure everything works as it should

- If you are the maintainer, close the relevent issues (by adding fix... in the commit message with --amend)

- If you are the maintainer, create the appropriate tag

        $ git tag <version>

- If you are the maintainer, push the code to any relevant remote

        $ git push
        
- If you are the maintainer, upload the code to PyPI

        $ python3 setup.py sdist
        $ twine upload dist/*
        
- If you are the maintainer, check that the docs are updated

- If you are the maintainer or the devops guy, deploy the new code to all relevant machines

