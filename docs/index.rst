.. locust-nest documentation master file, created by
   sphinx-quickstart on Wed May  9 11:37:52 2018.

locust-nest
===========
|license| |versions| |pypi| |contributors|

.. |license| image:: https://img.shields.io/github/license/ps-george/locust-nest.svg
  :alt: license
  :target: https://github.com/ps-george/locust-nest/blob/master/LICENSE

.. |versions| image:: https://img.shields.io/pypi/v/locust-nest.svg 
  :alt: PyPI
  :target: https://pypi.org/project/locust-nest/

.. |pypi| image:: https://img.shields.io/pypi/pyversions/locust-nest.svg
  :alt: PyPI
  :target: https://pypi.org/project/locust-nest/

.. |contributors| image:: https://img.shields.io/github/contributors/ps-george/locust-nest.svg
  :alt: GitHub contributors
  :target: https://github.com/ps-george/locust-nest/graphs/contributors

Locust wrapper. Import Locust classes from a folder and run Locust using those classes with weights determined in a config file,
with an option to guide the generation of the config file.

- `locust-nest docs`_
- `locust-nest pip package`_
- `locust-nest source code`_

`Locust.io`_
------------- 

- `Locust docs`_
- `Locust source code`_

.. _`locust-nest docs`: https://ps-george.github.io/locust-nest
.. _`locust-nest pip package`: https://pypi.org/project/locust-nest/
.. _`locust-nest source code`: https://github.com/ps-george/locust-nest

.. _`Locust.io`: https://locust.io
.. _`Locust docs`: https://docs.locust.io/en/stable/
.. _`Locust source code`: https://github.com/locustio/locust

What is locust-nest for?
========================

locust-nest is a wrapper around Locust to simplify load testing.

Use locust-nest for *load generation*.

Unit tests or live user testing will tell you if your system works for 1 user, locust-nest will show you if it can scale to 100, 1000 or 100,000 simultaneous users.

It allows you to configure the weighting of each of your Locust classes so that you can run different load scenarios without changing any Python code.

It will search sub-directories for Locust classes, so your :code:`models/` directory could contain git submodules with a number of Locust models.

Table of Contents
=================

.. toctree::
   :maxdepth: 2

   INSTALLATION
   QUICKSTART
   RATIONALE
   FAQ

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
