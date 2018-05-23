from locust import TaskSet, task, HttpLocust

class Model(TaskSet):
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
    
    @task(5) # task decorator with relative weight of executing the task
    def model_action(self):
        """Codified behaviour of a particular action this model may perform
        e.g. registering a customer

        """
        
        return

class ModelLocust(HttpLocust):
    task_set = Model
