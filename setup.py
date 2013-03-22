import os
from setuptools import setup, find_packages
import linklist as app


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


setup(
    name='cmsplugin-linklist',
    version=app.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='django, reusable, position, reorder, order',
    author='Tobias Lorenz',
    author_email='tobias.lorenz@bitmazk.com',
    url='https://github.com/bitmazk/cmsplugin-linklist',
    packages=find_packages(),
    include_package_data=True,
)
