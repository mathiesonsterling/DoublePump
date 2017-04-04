from abc import abstractmethod
from src.entities import TaskStatus

"""
Abstract class for Task objects
"""
class Task(object):

    def __init__(self):
        """
        How many times this instance has tried to do its work this time
        """
        self.number_of_times_tried = 0

        """
        How many times this instace will try to do its thing before going to failure
        """
        self.maximum_times_to_retry = 3

        self.error_message = ''

    @abstractmethod
    def get_status(self):
        if self.number_of_times_tried > self.maximum_times_to_retry:
            return TaskStatus.Failed()

    @abstractmethod
    def do(self, resourceDictionary):
        self.number_of_times_tried = self.number_of_times_tried

    @abstractmethod
    def get_dependent_tasks(self):
        return []

    @abstractmethod
    def get_name(self):
        raise StandardError("Name has not been set for task")

    def reset(self):
        self.number_of_times_tried = 0


