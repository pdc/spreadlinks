# Changelog

## 0.5.0 (2025-08-29)

### Changed

* Changed URLconf to be compatible with Django 5.x.
* Build with Poetry rather than Pipenv.
* Change licence to MIT (this is the default MIT-style licence on [choosealicence.com]).

### Deleted

* Removed support for Python 2.
* Removed spurious Lineform documents from packages.

[choosealicense.com]: https://choosealicense.com

## 0.4.1 (2020-05-25)

### Changed

* Change import for Python 3.9 compatibility
  (This breaks compatibility with Python ≤ 3.2).
* Move tests in to their own directory.

## 0.4.0

### Added

* Allow specification of style sheets to include on the pages.

### Changed

* Add more CSS class names to the HTML generated for the sake of better theming.

## 0.3.0

* Specify UTF-8 explicitly when decoding metadata file
  for Python-2 compatibility.
  Python 3 guesses based on LANG which is not necessarily defined.


## 0.2.3

### Changed

* Bug fix: Add `include_package_data` (not documented on https://packaging.python.org but
  used on https://docs.djangoproject.com/en/2.0/intro/reusable-apps/)


## 0.2.2

### Changed

* Bug fix: Add `package_data` directive so templates and static files are not forgotten.


## 0.2.1

### Changed

* Bug fix: Remove `$` from URLConf left over from the `url(...)` days.
