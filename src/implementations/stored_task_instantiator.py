from src.entities import TaskInstantiator
from src.implementations.testing import MustRunTask
from src.implementations.testing import ParentTask
"""
Holds all tasks as an instance, delivers them when asked
"""
class StoredTaskInstantiator(TaskInstantiator):
    def __init__(self):
        self.known_tasks = {}

    def instantiate_task(self, task_name):
        if task_name in self.known_tasks.keys():
            raise LookupError("The task " + task_name + " is already stored")
        return self.known_tasks[task_name]

    def add_task_instance(self, task):
        self.known_tasks[task.get_name()] = task