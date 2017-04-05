from src.entities import Task
from src.entities import TaskStatus
import os

class CommandLineTask(Task):

    def __init__(self, command, task_name, expected_return_code=0):
        super(CommandLineTask, self).__init__()
        self.task_name = task_name
        self.command_string = command
        self.return_code = None
        self.expected_return_code = expected_return_code

    def get_dependent_tasks(self):
        return []

    def do(self, resourceDictionary):
        super(CommandLineTask, self).do(resourceDictionary)

        self.return_code = os.system(self.command_string)

    def get_name(self):
        return self.task_name

    def get_status(self):
        status = super(CommandLineTask, self).get_status()

        if status is TaskStatus.Failed():
            return status

        if self.return_code is None:
            return TaskStatus.NeedsToBeDone()
        else:
            if self.return_code == self.expected_return_code:
                return TaskStatus.Done()


