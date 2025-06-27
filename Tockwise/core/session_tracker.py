import time

class SessionTracker:
    def __init__(self):
        self.start_time = None

    def start_session(self):
        self.start_time = time.time()

    def end_session(self):
        if self.start_time:
            duration = time.time() - self.start_time
            return duration
        return 0
