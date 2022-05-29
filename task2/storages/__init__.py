from abc import ABC, abstractmethod


class Storage(ABC):
    config = None

    def __init__(self, config):
        self.config = config

    @abstractmethod
    def create_record(self):
        pass