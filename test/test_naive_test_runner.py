import unittest
from src.implementations.testing import MustRunTask
from src.implementations import NaiveTaskRunner
from src.implementations import StoredTaskInstantiator
from src.implementations import ConsoleLogger
from src.implementations.testing import ParentTask

class TestNaiveTestRunner(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_single_task(self):
        task = MustRunTask()

        instant = StoredTaskInstantiator()
        instant.add_task_instance(task)

        logger = ConsoleLogger()
        runner = NaiveTaskRunner(instant, logger)

        runner.run_task(task)

    def test_task_with_dependencies(self):
        task = ParentTask()

        instant = StoredTaskInstantiator()
        instant.add_task_instance(task)
        instant.add_task_instance(MustRunTask())

        logger = ConsoleLogger()
        runner = NaiveTaskRunner(instant, logger)

        runner.run_task(task)