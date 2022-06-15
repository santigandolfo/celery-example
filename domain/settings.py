import os


class REDIS:
    def __init__(self):
        self.HOST = os.environ['REDIS_HOST']
        self.PORT = int(os.environ['REDIS_PORT'])
        self.TIMEOUT = int(os.environ['REDIS_TIMEOUT'])
