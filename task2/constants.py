from task2.record_creator.json_record_creator import JsonRecordCreator
from task2.record_creator.xml_record_creator import XMLRecordCreator
from task2.storages.aws_s3_storage import AwsS3Storage
from task2.storages.local_storage import LocalStorage

"""
--- available data formats
new data formats can be added this list to expand the library
"""
available_formats = ["json", "xml"]

# new record creator classes can be implemented and added this map
data_creator_mapper = {
    "json": JsonRecordCreator,
    "xml": XMLRecordCreator
}

"""
--- available storage types
new storage types can be added this list to expand the library
"""
available_storage_types = ["local", "aws_s3"]

# new storage classes can be implemented and added this map
storage_generator_mapper = {
    "local": LocalStorage,
    "aws": AwsS3Storage
}