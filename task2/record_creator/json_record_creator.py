from task2.record_creator import RecordCreator
from task2.record_creator.record.json_record import JsonRecord


class JsonRecordCreator(RecordCreator):

    def __init__(self, name, data):
        super().__init__(name, data)

    def create_record(self):
        return JsonRecord(name=self.name, data=self.data)