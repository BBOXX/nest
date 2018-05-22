Aims of Nest
==============
Predict future scalability requirements and cost per customer.

Nest Prouduct Management 
--------------------------

The information gained from Nest is incredibly useful for proactive product management, helping to guide long-term architectural decisions and avoid a false economy of technical debt due to decisions guided by a lack of knowledge about the future strains on the system. On a day-to-day basis this could be used to prevent unscalable code changes from being deployed into production either to be immediately reverted due to the lack of a full-load simulation, or several months later when usage has grown. 

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


Under the hood
~~~~~~~~~~~~~~

Task weighting is done by populating the task list with X of each task, where X is that task's weight (defaulting to 1), and during the scheduling phase using `random.choice` to pick the next task to schedule. This is an elegantly simple way of doing this that works well without requiring any external packages (numpy.random has this functionality).

The wait inbetween each executing task is determined using `random.randint(self.min*wait,self.max*wait)`, which gives a uniformly distributed wait time between each task within the bounds. It would be nice to be able to customise this with a function that gives an exponential wait time between the minimum and maximum to give a more realistic distribution, or allow user defined functions so that any distribution can be used to sample interarrival times of tasks. In most real world situations, inter-arrival times approximate to exponential distributions and it is a shame that locust cannot model this. I've submited a pull request to ammend this and allow any user-defined wait function to be used. Pull request merged! ...


Locust was chosen because it is:
1. All in Python. Since our codebase is Python it makes it easy to write tests alongside development. No need to learn a DSL or 'code' XML.
2. Actively supported.
3. Simple but able to simulate any situation.
4. Possible to run distributed with master-slave configuration.

Disadvantages
~~~~~~~~~~~~~

1. No [per locust hatching](https://github.com/locustio/locust/pull/712). Will need to test this PR, improve it if possible and get Owner to merge.

2. No framework for automatically provisioning and deploying a distributed network of locusts from a server-configuration point of view. This would be interesting to develop (using Serverless, AWS Lambda and so on).

3. [invokust](https://github.com/FutureSharks/invokust) is a good idea but needs some improvement to allow access to all settings. Currently doesn't allow master-slave settings to be set.

Alternatives to Locust
~~~~~~~~~~~~~~~~~~~~~~

Other load testing frameworks are:

Grinder, JMeter, Gatling
ab, Siege, beeswithmachineguns, Multi-Mechanize, httperf 



