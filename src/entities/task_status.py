class TaskStatus(object):
    @staticmethod
    def Done():
        return "Done"
    @staticmethod
    def Failed():
        return "Failed"
    @staticmethod
    def NeedsToBeDone():
        return "NeedsToBeDone"