from src.entities import Task
from src.entities import TaskStatus

"""A simple task which sets itself to run after being told to do so
"""
class MustRunTask(Task):
    def __init__(self):
        super(MustRunTask, self).__init__()
        self.was_called = False

    def get_status(self):
        failed = super(MustRunTask, self).get_status()
        if failed == TaskStatus.Failed():
            return TaskStatus.Failed()

        if self.was_called:
            return TaskStatus.Done()
        else:
            return TaskStatus.NeedsToBeDone()

    def do(self, resource_dictionary):
        super(MustRunTask, self).do(resource_dictionary)

        self.was_called = True

    def get_name(self):
        return "MustRunTask"

