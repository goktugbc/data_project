import json

from task2.record_creator.record import Record
from task2.record_creator.record.exceptions import WrongFormatException


class JsonRecord(Record):

    def __init__(self, name, data):
        super().__init__(name, data)
        self.filename = self.name + ".json"

    def dump_data(self):
        try:
            return json.dumps(self.data)
        except TypeError:
            raise WrongFormatException("Data you are trying to dump is in wrong format.")

    def load_data(self):
        try:
            return json.loads(self.data)
        except TypeError:
            raise WrongFormatException("Data you are trying to load is in wrong format.")

