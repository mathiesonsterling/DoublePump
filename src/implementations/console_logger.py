from src.services import Logger


class ConsoleLogger(Logger):
    def log_message(self, message):
        print message
