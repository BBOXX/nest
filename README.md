# Project nest
Import tasksets from a 'tasksets/' folder into a common class and run Locust using that class.

## Directory structure

- docs: documentation
- tasksets: directory for tasksets 

## How to use

Project Nest is designed to provide a framework for simulating a specified load on a system.

Behaviour models are codified using Locust, an open-source load testing tool that allows abitrarily complex user behaviour modelling since all tasks are written in Python. 

This system works by searching all `.py` files in the `tasksets` directory and subdirectories for subclasses of `TaskSet` and adding these to a `NestTaskset`, which packages all the tasks with their desired weights into a `HTTPLocust` class. Note: Python 2 does not have support for recursive subdirectories, so only searchs 1 directory deep `tasksets/*/`

To run project nest, simply use nest.py as your locustfile:
```bash
locust -f nest.py --host=https://www.example.com ...
```

To be guided through the generation of a config file, run:
```bash
python configure.py
```

An example structure for one of these TaskSets is:
```python
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
```

# Configure.py

Separate program: config.py: ask user for each taskset the different weightings to use, and ask if you'd like to save these to a config file.

## Workflow

1. Nest will import all TaskSets from `tasksets/`
2. Run any dependencies e.g. flask webserver for shared data between Locusts.
3. Using the values in the config file (or 'Get config from sub-tasksets' setting), assign the various weights.
4. Display weightings that will be used with confirmation prompt (skippable with some commandline argument).
4. Run Locust with weightings set from config (thoughts on how to run this using AWS Lambda/etc)
