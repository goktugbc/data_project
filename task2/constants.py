#available data formats
from task2.record_creator.json_record_creator import JsonRecordCreator
from task2.storages.local_storage import LocalStorage

available_formats = ["json"]

data_creator_mapper = {
    "json": JsonRecordCreator
}

available_storage_types = ["local"]

storage_generator_mapper = {
    "local": LocalStorage
}