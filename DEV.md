Developer notes
===============

The file `Pipfile` is included as a convenience when developing; the
dependencies for the app are specified in `setup.py`.


Tests
-----

These are in their own package:

    pipenv run python -m unittest discover


Release process
----------------

Update CHANGELOG.md

Update `setup.py`:

* Possibly bump `__version__` minor version
* Remove `.dev` from `setuptools.setup`

Build and publish

    rm -rf dist Spreadlinks.egg-info/SOURCES.txt &&
    pipenv run python setup.py sdist bdist_wheel &&
    pipenv run twine upload dist/*

* Bump version to next patchlevel
* Reinstate `.dev`
