# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='punisfun',
    version='0.0.1',
    description='A solution to the pun detection task of Semeval 2017',
    long_description=readme,
    author='Parag Guruji',
    author_email='pguruji@purdue.edu',
    url='https://github.com/paragguruji/punisfun',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
