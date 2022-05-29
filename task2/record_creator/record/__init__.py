from abc import ABC, abstractmethod


class Record(ABC):
    name = ""
    data = None

    def __init__(self, name, data):
        self.name = name
        self.data = data

    @abstractmethod
    def generate_file(self):
        pass

    @abstractmethod
    def delete_file(self):
        pass

    @abstractmethod
    def dump_data(self):
        pass

    @abstractmethod
    def load_data(self):
        pass
