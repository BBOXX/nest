locust-nest
===========
Documentation_

.. _Documentation: https://ps-george.github.io/locust-nest

Import tasksets from a 'tasksets/' folder into a common class and run Locust using that class.

Installation
============

.. code-block:: bash

    pip install locust-nest

Note: This package depends on a cutting edge version of locust that has not been merged into the master repo or released yet.

Quick start
===========

locust-nest is designed to provide a framework for simulating a specified load on a system.

Behaviour models are codified using Locust, an open-source load testing tool that allows abitrarily complex user behaviour modelling since all tasks are written in Python. 

This system works by searching all `.py` files in the `tasksets` directory and subdirectories for subclasses of `TaskSet` and adding these to a `NestTaskset`, which packages all the tasks with their desired weights into a `HTTPLocust` class. Note: Python 2 does not have support for recursive subdirectories, so only searchs 1 directory deep `tasksets/*/`

To run locust-nest, simply use locust-nest command with default Locust arguments:

.. code-block:: bash

  locust-nest --taskset_dir=tasksets/ --host=https://www.example.com ...

To be guided through the generation of a config file before running locust-nest as usual, run: 

.. code-block:: bash

  locust-nest --configure ...

An example structure for one of these TaskSets is:

.. code-block:: python

  from locust import TaskSet, task

  class ModelBehaviour(TaskSet):
    weight = 0
    def on_start(self):
      # Log in & save token

      # retrieve bulk information needed for other tasks

      # other to-dos on starting this group of tasks
      pass

    def on_stop(self):
      # unclaim resources e.g. username
      pass
    
    @task(5) # task decorator with relative weight of executing the task
    def model_action(self):
      # codified behaviour of a particular action this model may perform
      # e.g. registering a customer
      return

    @task(1)
    def stop(self): # Kill this process and choose another from the tasksets folder
      self.interrupt()
    
configure flag
----------------
Ask user for each taskset the different weightings to use, and ask if you'd like to save these to a config file.

Workflow
~~~~~~~~

1. Nest will import all TaskSets from `tasksets/`
2. Run any dependencies e.g. flask webserver for shared data between Locusts. (NOT IMPLEMENTED.)
3. Using the values in the config file (or 'Get config from sub-tasksets' setting), assign the various weights.
4. Display weightings that will be used with confirmation prompt (skippable with some commandline argument).
5. Run Locust with weightings set from config (thoughts on how to run this using AWS Lambda/etc)

Example TaskSet
~~~~~~~~~~~~~~~
.. code-block:: python

    from locust import TaskSet, task

    class ExampleModel(TaskSet):
        weight = 0

        def on_start(self):
            """Set up before running tasks.

            For example:
            * Log in & save token
            * Retrieve bulk information needed for other tasks

            """
            return

        def on_stop(self):
            """Teardown: unclaim resources e.g. claimed user.

            """

            return

        # task decorator with relative weight of executing the task
        @task(5) 
        def model_action(self):
            """Codified behaviour of a particular action this model may perform
            e.g. registering a customer

            """
            self.client.get("/")
            return


Aims of locust-nest
===================

1. Users will be able to place any number of directories containing TaskSets, 
   with each TaskSet representing an encapsulated group of tasks.
2. locust-nest will find all TaskSets contained in a specified directory
   and group them into one Locust class with corresponding weights specified
   in a config file, allowing easy modularity in adding or removing TaskSets
   without needing to change any code in the locust-nest repository.
3. There will be an interactive configure option which creates a config file
   that specifies the relative weights of each TaskSet, allowing users to easily
   adjust the different ratios of TaskSet types, but still allowing non-interactive 
   use of the system when the config file has been created.
4. locust-nest will be automatable, ideally callable with a git hook for load-testing
   continuous integration or in response to a Slack command. The results will be human readable,
   ideally some kind of index of scalability of the system, so that the evolution of the system
   under test's scalability can be tracked.
5. locust-nest will be able to automatically deploy to AWS Lambda or equivalent and
   run load testing under the distributed master-slave variant in order to be able
   to easily scale arbitrarily.
   