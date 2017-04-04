import unittest
from src.implementations import MustRunTask
from src.implementations import NaiveTaskRunner
from src.implementations import StoredTaskInstantiator
from src.implementations import ConsoleLogger
from src.implementations import ParentTask

class TestNaiveTestRunner(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_single_task(self):
        task = MustRunTask()

        instant = StoredTaskInstantiator()
        logger = ConsoleLogger()
        runner = NaiveTaskRunner(instant, logger)

        runner.run_task(task)

    def test_task_with_dependencies(self):
        task = ParentTask()

        instant = StoredTaskInstantiator()
        logger = ConsoleLogger()
        runner = NaiveTaskRunner(instant, logger)

        runner.run_task(task)