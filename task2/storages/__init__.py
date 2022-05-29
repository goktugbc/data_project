from abc import ABC, abstractmethod


class Storage(ABC):
    config = None

    def __init__(self, config):
        self.config = config

    @abstractmethod
    def get_storage(self):
        pass

    @abstractmethod
    def get_record_from_file(self):
        pass

    @abstractmethod
    def check_record_exists(self, filename):
        pass

    @abstractmethod
    def insert_record(self, record):
        pass

    @abstractmethod
    def insert_records(self, records):
        pass

    @abstractmethod
    def retrieve_record(self, filename):
        pass

    @abstractmethod
    def filter_records(self, record_format, limit, offset):
        pass

    @abstractmethod
    def update_record(self, filename, record):
        pass

    @abstractmethod
    def delete_record(self, filename):
        pass
