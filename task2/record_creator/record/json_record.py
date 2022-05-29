import json

from task2.record_creator.record import Record
from task2.record_creator.record.exceptions import WrongFormatException


class JsonRecord(Record):

    def __init__(self, name, data):
        super().__init__(name, data)

    def generate_file(self):
        import os

        tmp_path = "tmp/"

        if not os.path.exists(tmp_path):
            os.makedirs(tmp_path)

        filename = self.name + ".json"
        f = open(tmp_path + filename, "w")
        f.write(self.dump_data())
        f.close()

    def delete_file(self):
        import os
        filename = self.name + ".json"
        os.remove("tmp/" + filename)

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

