from task2 import constants
from task2.storages import Storage
from task2.storages.exceptions import WrongConfigException, StorageOperationError, RecordNotFound, \
    LimitOffsetIncompatibility


class LocalStorage(Storage):
    local_path = ""

    def __init__(self, config):
        super().__init__(config)

    def get_storage(self):
        if "path" not in self.config:
            raise WrongConfigException

        import os

        if not os.path.exists(self.config["path"]):
            os.makedirs(self.config["path"])

        if self.config["path"].endswith("/"):
            self.local_path = self.config["path"]
        else:
            self.local_path = self.config["path"] + "/"

        return self

    def check_record_exists(self, filename):
        from os.path import exists

        return exists(self.local_path + filename)

    def get_record_from_file(self, filename):
        name = ".".join(filename.split(".")[:-1])
        record_format = filename.split(".")[-1]
        f = open(self.local_path + filename, "r")
        data = f.read().strip()

        record = constants.data_creator_mapper[record_format](name, data).create_record()
        record.data = record.load_data()

        return record

    def insert_record(self, record):
        import os

        tmp_file = record.generate_file()
        try:
            os.replace(tmp_file, self.local_path + record.filename)
        except Exception:
            raise StorageOperationError("Insert operation cannot be done.")

    def insert_records(self, records):
        for record in records:
            self.insert_record(record)

    def retrieve_record(self, filename):
        if not self.check_record_exists(filename):
            raise RecordNotFound
        else:
            try:
                record = self.get_record_from_file(filename)
            except Exception:
                raise StorageOperationError("Retrieve operation cannot be done.")

            return record

    def filter_records(self, record_format, limit, offset):
        import os

        record_names = []
        records = []

        for file in os.listdir(self.local_path):
            if file.endswith("." + record_format):
                record_names.append(file)

        record_names.sort()

        if limit is None:
            limit = len(record_names)

        if offset > limit:
            raise LimitOffsetIncompatibility

        record_names = record_names[offset:limit]

        for record_name in record_names:
            records.append(self.retrieve_record(record_name))

        return records

    def update_record(self, filename, record):
        if not self.check_record_exists(filename):
            raise RecordNotFound
        else:
            try:
                self.delete_record(filename)
                self.insert_record(record)
            except Exception:
                raise StorageOperationError("Update operation cannot be done.")

    def delete_record(self, filename):
        if not self.check_record_exists(filename):
            raise RecordNotFound
        else:
            import os
            try:
                os.remove(self.local_path + filename)
            except Exception:
                raise StorageOperationError("Delete operation cannot be done.")
