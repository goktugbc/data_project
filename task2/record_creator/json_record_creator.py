from task2.record_creator import RecordCreator
from task2.record_creator.record.json_record import JsonRecord


class JsonRecordCreator(RecordCreator):

    def __init__(self):
        super().__init__()

    def create_record(self, name, data):
        return JsonRecord(name=name, data=data)
