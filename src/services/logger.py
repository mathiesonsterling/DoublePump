from abc import abstractmethod

class Logger(object):
    @abstractmethod
    def log_message(self):
        raise StandardError("Function not implemented")