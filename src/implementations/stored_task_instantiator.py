from src.entities import TaskInstantiator
from src.implementations.testing import MustRunTask
from src.implementations.testing import ParentTask
"""
Holds all tasks as an instance, delivers them when asked
"""
class StoredTaskInstantiator(TaskInstantiator):
    def __init__(self):
        self.known_tasks = [
            MustRunTask(),
            ParentTask()
        ]

    def instantiate_task(self, task_name):
        for task in self.known_tasks:
            if task.get_name() == task_name:
                return task
        return None