locust-nest
===========
Import tasksets from a 'tasksets/' folder into a common class and run Locust using that class.

Installation
============

This package depends on a cutting edge version of locust that has not been merged into the master repo or released yet.

.. code-block:: bash

    pip install -e git://github.com/ps-george/locust.git@master#egg=locustio
    pip install locust-nest

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
    
--configure flag
----------------
Ask user for each taskset the different weightings to use, and ask if you'd like to save these to a config file.

Workflow
~~~~~~~~

1. Nest will import all TaskSets from `tasksets/`
2. Run any dependencies e.g. flask webserver for shared data between Locusts.
3. Using the values in the config file (or 'Get config from sub-tasksets' setting), assign the various weights.
4. Display weightings that will be used with confirmation prompt (skippable with some commandline argument).
4. Run Locust with weightings set from config (thoughts on how to run this using AWS Lambda/etc)

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
==============================
Predict future scalability requirements and cost per customer.

Nest Prouduct Management 
--------------------------

The information gained from locust-nest is incredibly useful for proactive product management, helping to guide long-term architectural decisions and avoid a false economy of technical debt due to decisions guided by a lack of knowledge about the future strains on the system. On a day-to-day basis this could be used to prevent unscalable code changes from being deployed into production either to be immediately reverted due to the lack of a full-load simulation, or several months later when usage has grown. 

As a Nest product manager, you will have a crystal ball into the future burdens on your system and be able to plan proactively.

Justify long-term decisions
~~~~~~~~~~~~~~~~~~~~~~~~~~~
The pain points of maintaining a monolithic architecture are well documented [1]_, however it is difficult to justify migration when *it works* and there is no information as to future running costs and maintenence needs.

Without evidence that continual development will be required to keep the system running as it scales, there is no justification for redeveloping and migrating parts of the system to a non-monolithic architecture because the performance and problems of the system under *future* load are not known.

The problem is that being unable to simulate future load means product development must always be reactive to scaling issues, only being able to look one step ahead when making architectural decisions and hampering the ability to plan effectively for the future.

.. [1] Steeper learning curve for new starters, prerequisite knowledge of all parts in order to debug or make changes, harder to test new functionality, hard to pinpoint pinch points or replace consituent parts. 

Optimise Financial Decisions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Obtain a detailed breakdown of the various cost drivers, helping with pricing (for example per 1000 customers) and a good model for system behaviour would be able to predict how other financial decisions (for example increasing the minimum payment amount) affect the load on the system. Such a framework for simulating load would make it possible to explore different server configurations and compare the costs and performance of each without having to deploy a live instance into production. 

Fearless battle-tested deployment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This also provides a platform for developing new systems, giving a reliable benchmark for performance under load. It might seem like a good idea to slice out some functionality and move it into an AWS Lambda serverless instance or Webtask, but do you really want to live test such a move? With a model for simulating customer load on the system one can get an accurate representation of whether it will actually improve costs and performance, or suffer from the same problems as before. In fact, it is often the lack of such information that paralyses architectural innovation since it becomes too risky.

Requirements
------------
1. Easy to extend.
2. Scalable (no point writing a load testing system that cannot scale to the load testing that is required).
3. Version controllable
4. Open Source 
5. Developer friendly (easy to code updated behaviour into the model whilst writing it)
6. Automatable; no manual configuration required for each launch
7. Modular (adding/removing behaviour is easy)
8. Flexible
9. Intuitive results (nice graphical representation/comparison).

Why Locust?
-----------
Locust is an open source Python framework for writing load tests. 

1. High scalability locally due to events based implementation 
2. Can run distributed with many agents.
3. Flexible; All tests are written in code, can model any behaviour.
4. All in Python, no messing around with XML, DSLs or GUIs.
5. Easily version controlled.

Off the bat Locust provides functionality for nearly all of the requirements for this project, which is why it was chosen over any alternatives.

Locust was chosen because it is:
1. All in Python. Since our codebase is Python it makes it easy to write tests alongside development. No need to learn a DSL or 'code' XML.
2. Actively supported.
3. Simple but able to simulate any situation.
4. Possible to run distributed with master-slave configuration.
