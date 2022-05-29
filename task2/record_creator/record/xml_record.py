import json

from task2.record_creator.record import Record
from task2.record_creator.record.exceptions import WrongFormatException


class XMLRecord(Record):

    def __init__(self, name, data):
        super().__init__(name, data)
        self.filename = self.name + ".xml"

    def dump_data(self):
        print("not implemented")

    def load_data(self):
        print("not implemented")

