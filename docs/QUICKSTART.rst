.. _quickstart-label:

Quick start
===========

locust-nest is designed to provide a framework for simulating a specified load on a system.

Behaviour models are codified using Locust, an open-source load testing tool that allows abitrarily complex user behaviour modelling since all tasks are written in Python. 

This wrapper searches all `.py` files in the :code:`--model_dir (-d)` directory and subdirectories for subclasses of `Locust` and runs Locust with all of those classes.

To run locust-nest, simply use locust-nest command with default Locust arguments:

.. code-block:: bash

  locust-nest --model_dir=models/ --host=https://www.example.com ...

To be guided through the generation of a config file, use the :code:`--configure` flag: 

.. code-block:: bash
  
  locust-nest --configure --host=https://www.example.com ...


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
    

If the :code:`--include-tasksets (-T)` flag is used, it will also find all subclasses of `TaskSet` and add these to a `NestTaskset`,
which packages all the tasks with their desired weights into a `HTTPLocust` class.
of those classes, with weights specified in a :code:`--config_file`.
Note: Python 2 does not have support for recursive subdirectories, so at the moment only searches 1 directory deep :code:`{model_dir}/*/`

configure flag
----------------
Ask user for each taskset the different weightings to use, and ask if you'd like to save these to a config file.

Workflow
~~~~~~~~

1. Nest will import all TaskSets from `models/` into one NestLocust, weighting according to :code:`--config_file`.
2. Nest will find all Locust's, weighting according to :code:`--config_file`.
3. Run any dependencies e.g. flask webserver for shared data between Locusts. (NOT IMPLEMENTED.)
4. Display weightings that will be used with confirmation prompt (skippable with some commandline argument).
5. Run Locust with weightings set from config for the Locusts and NestLocust classes
6. Nest will have an option to automatically manage distributed resources for Locust master-slave mode. (NOT IMPLEMENTED)

Example TaskSet
~~~~~~~~~~~~~~~

.. literalinclude:: ../models/example.py
  :language: python
  :linenos:
