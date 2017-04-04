from abc import abstractmethod

class TaskInstantiator(object):
    @abstractmethod
    def instantiate_task(self, task_name): pass