class TaskRunReport(object):
    def __init__(self, success):
        self.success = success
        self.error_messages = []