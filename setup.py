"""Metadata for the Spreadlinks library."""

import setuptools

with open('README.md', 'r') as input:
    long_description = input.read()

setuptools.setup(
    name='Spreadlinks',
    version='0.1.0.dev',
    author='Damian Cugley',
    author_email='pdc@alleged.org.uk',
    description='A Django app for serving libraries of links from spreadsheets.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/pdc/spreadlinks',
    packages=setuptools.find_packages(),
    install_requires=[
        'Markdown',
    ],
    classifiers=(
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
