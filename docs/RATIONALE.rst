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