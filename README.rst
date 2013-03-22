CMSplugin Linklist
==================

Django-cms plugin to render a list of detailed links.

Prerequisites
-------------

You need at least the following packages in your virtualenv:

* Django 1.4
* South
* Django-CMS
* Filer
* Pillow or PIL
* Easy Thumbnails


Installation
------------

To get the latest stable release from PyPi::

    $ pip install cmsplugin-linklist (not available at the moment)

To get the latest commit from GitHub::

    $ pip install -e git://github.com/bitmazk/cmsplugin-linklist.git#egg=linklist

Add the app to your ``INSTALLED_APPS``::

    INSTALLED_APPS = [
        ...
        'django',
        'cms',
        'menus',
        'mptt',
        'sekizai',
        'filer',
        'easy_thumbnails',
        'linklist',
    ]

Run the south migrations to create the app's database tables::

    $ ./manage.py migrate linklist


Usage
-----

Just create a cms page and add the plugin to a placeholder field.


Roadmap
-------

See the issue tracker for current and upcoming features.
