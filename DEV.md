


Release process
----------------

Update `setup.py`:

* Possibly `__version__` minor version
* Remove `.dev` from `setuptools.setup`

Build and publish

    rm -rf dist Spreadlinks.egg-info/SOURCES.txt &&
    pipenv run python setup.py sdist bdist_wheel &&
    pipenv run twine upload dist/*

* Bump version to next patchlevel
* Reinstate `.dev`
