from task2 import constants
from task2.storages import Storage
from task2.storages.exceptions import WrongConfigException, StorageOperationError, RecordNotFound, \
    LimitOffsetIncompatibility


class AwsS3Storage(Storage):
    aws_connection = ""

    def __init__(self, config):
        super().__init__(config)

    def get_storage(self):
        # AWS S3 connection must be implemented and aws_connection must be initialized
        print("not implemented")
        return self

    def check_record_exists(self, filename):
        print("not implemented")

    def get_record_from_file(self, filename):
        print("not implemented")

    def insert_record(self, record):
        print("not implemented")

    def insert_records(self, records):
        print("not implemented")

    def retrieve_record(self, filename):
        print("not implemented")

    def filter_records(self, record_format, limit=None, offset=0):
        print("not implemented")

    def update_record(self, filename, record):
        print("not implemented")

    def delete_record(self, filename):
        print("not implemented")
