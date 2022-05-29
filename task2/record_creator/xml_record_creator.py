from task2.record_creator import RecordCreator
from task2.record_creator.record.xml_record import XMLRecord


class XMLRecordCreator(RecordCreator):

    def __init__(self):
        super().__init__()

    def create_record(self, name, data):
        return XMLRecord(name=name, data=data)
