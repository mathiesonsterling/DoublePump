from abc import abstractmethod


class TaskRunner(object):

    def __init__(self):
        self.resource = {}

    """
    Runs a given task, and all its dependencies
    """
    @abstractmethod
    def run_task(self, task): pass

    def set_resource(self, resource):
        self.resource = resource

    def get_resource(self):
        return self.resource

