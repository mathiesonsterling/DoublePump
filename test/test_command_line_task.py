import unittest
from src.implementations.built_in_tasks import CommandLineTask
from src.implementations import NaiveTaskRunner
from src.implementations import StoredTaskInstantiator
from src.implementations import ConsoleLogger

class TestCommandLineTask(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_single_task(self):
        task = CommandLineTask("echo howdy", "EchoTest")

        instant = StoredTaskInstantiator()
        instant.add_task_instance(task)

        logger = ConsoleLogger()
        runner = NaiveTaskRunner(instant, logger)

        runner.run_task(task)