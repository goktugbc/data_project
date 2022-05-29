from abc import ABC, abstractmethod


class RecordCreator(ABC):
    name = ""
    data = None
    filename = ""

    def __init__(self, name, data):
        self.name = name
        self.data = data

    @abstractmethod
    def create_record(self):
        pass