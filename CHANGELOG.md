Change log
==========

0.4.0
----

* Allow specification of style sheets to include on the pages.
* Add more CSS class names to the HTML generated for the sake of better theming,

0.3.0
-----

* Specify UTF-8 explicitly when decoding metadata file
  for Python-2 compatibility.
  Python 3 guesses based on LANG which is not necessarily defined.


0.2.3
------

* Bug fix: Add `include_package_data` (not documented on https://packaging.python.org but
  used on https://docs.djangoproject.com/en/2.0/intro/reusable-apps/)


0.2.2
-----

* Bug fix: Add `package_data` directive so templates and static files are not forgotten.


0.2.1
-----

* Bug fix: Remove `$` from URLConf left over from the `url(...)` days.
