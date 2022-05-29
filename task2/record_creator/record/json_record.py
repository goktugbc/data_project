import json

from task2.record_creator.record import Record
from task2.record_creator.record.exceptions import WrongFormatException


class JsonRecord(Record):

    def __init__(self, name, data):
        super().__init__(name, data)

    def generate_file(self):
        pass

    def dump_data(self):
        try:
            return json.dumps(self.data)
        except TypeError as e:
            raise WrongFormatException("Data you are trying to dump is in wrong format.")

    def load_data(self):
        try:
            return json.loads(self.data)
        except TypeError as e:
            raise WrongFormatException("Data you are trying to load is in wrong format.")

