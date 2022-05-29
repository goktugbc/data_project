from abc import ABC, abstractmethod


class RecordCreator(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def create_record(self, name, data):
        pass