from src.entities import TaskRunner
from src.entities import TaskStatus
from src import TaskError

"""
Very basic runner that just runs things in a single thread
"""


class NaiveTaskRunner(TaskRunner):
    def __init__(self, task_instantiator, logger):
        super(NaiveTaskRunner, self).__init__()
        self.task_instantiator = task_instantiator
        self.logger = logger

    def run_task(self, task):
        # get dependencies
        tasks = {}
        self.get_task_dependencies(task, tasks)

        for key in tasks:
            task = tasks[key]
            self.logger.log_message("Running task " + task.get_name())
            task.reset()
            while task.get_status() == TaskStatus.NeedsToBeDone():
                task.do(self.resource)

            if task.get_status() == TaskStatus.Failed():
                raise TaskError(task.error_message)

    def get_task_dependencies(self, task, found_tasks):

        this_level = task.get_dependent_tasks()

        for dep_name in this_level:
            # if we don't have the task already here, we need to add it
            if not self.task_name_in_list(dep_name, found_tasks):
                this_task = self.task_instantiator.instantiate_task(dep_name)
                found_tasks[this_task.get_name()]= this_task
                self.get_task_dependencies(this_task, found_tasks)

        if not self.task_name_in_list(task.get_name(), found_tasks):
            found_tasks[task.get_name()] = task

    def task_name_in_list(self, name, tasks):
        return name in tasks.keys()
