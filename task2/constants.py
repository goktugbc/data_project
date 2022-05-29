#available data formats
from task2.record_creator.json_record_creator import JsonRecordCreator

available_formats = ["json"]

data_creator_mapper = {
    "json": JsonRecordCreator
}