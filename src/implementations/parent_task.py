from src.entities import Task
from src.implementations import MustRunTask

class ParentTask(MustRunTask):
    def get_dependent_tasks(self):
        return ["MustRunTask"]

    def get_name(self):
        return "ParentTask"