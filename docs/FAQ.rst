.. _faq-label:

FAQ
===

Where can I find an example file?
---------------------------------

Run :code:`locust-nest install [dirname]` to create example files in that directory for locust-nest load testing.

How do I run a test?
--------------------

1. Create a .py file containing a Locust class.
2. Run the following:

.. code-block:: bash

    locust-nest [options]

What are the [options]?
-----------------------

--model-dir
^^^^^^^^^^^
:code:`-d {dirname}` or :code:`--model-dir={dirname}`

The directory containing Locust classes and/or TaskSets.

--configure
^^^^^^^^^^^
:code:`--configure`

Run a configuration helper that will create a config json file.

--config-file
^^^^^^^^^^^^^
:code:`--config-file`

The location of the config file to use.
If a config file is not found, locust-nest will use the weights specified in the classes.

--include-tasksets
^^^^^^^^^^^^^^^^^^
:code:`-T` or :code:`--include-tasksets`

Make a Locust for the TaskSets with ratios from the config file.

Locust options
^^^^^^^^^^^^^^

After locust-nest options, the program will parse Locust options and implement them as well. The `--host` option is required if the host is not specified in all of the Locust classes.

:code:`--no-web --clients=X --hatch-rate=X --run-time=30s --csv-base-name={filename}` are useful options for automating testing.

View Locust options using :code:`locust -h`.

How do I test something that is not web-based?
----------------------------------------------
Tests can be any Python code.
Just use the :code:`@task(1)` wrapper around a function in a TaskSet to identify it as a test.
See extending-locust_ for more on using Locust to test other clients.

.. _extending-locust: https://docs.locust.io/en/stable/extending-locust.html

How can I ensure my tests are the same each time?
-------------------------------------------------

Create a bash script to save the arguments you used.
Commit the script and config file to version control.

How do I compare two versions of a system?
------------------------------------------

Run locust-nest on both with the same settings for a fixed time and compare the outputs.

