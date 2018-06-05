from locust import TaskSet, task, HttpLocust


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


class ExampleModelLocust(HttpLocust):
    host = "http://127.0.0.1:8089"
    task_set = ExampleModel
