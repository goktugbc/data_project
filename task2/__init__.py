from . import constants

__version__ = "1.0.0"

from task2.exceptions import UnsupportedFormatException, UnsupportedStorageTypeException

Version = __version__


def create_record(record_format, name, data):
    if record_format not in constants.available_formats:
        raise UnsupportedFormatException

    return constants.data_creator_mapper[record_format]().create_record(name, data)


def get_storage(type, config):
    if type not in constants.available_storage_types:
        raise UnsupportedStorageTypeException

    return constants.storage_generator_mapper[type](config).get_storage()


def insert_record(storage, record):
    storage.insert_record(record)


def insert_records(storage, records):
    storage.insert_records(records)


def retrieve_record(storage, filename):
    storage.retrieve_record(filename)


def filter_records(storage, record_format, limit=None, offset=0):
    storage.filter_records(record_format, limit, offset)


def update_record(storage, filename, record):
    storage.update_record(filename, record)


def delete_record(storage, filename):
    storage.delete_record(filename)
