import constants

__version__ = "1,0,0"

from task2.exceptions import UnsupportedFormatException

Version = __version__

def create_record(format, name, data):
    if format not in constants.available_formats:
        raise UnsupportedFormatException

    return constants.data_creator_mapper[format](name, data).create_record()

def get_storage():
    pass

def insert_record(record):
    pass

def insert_records(records):
    pass

def retrieve_record(name):
    pass

def filter_records(format, limit, offset):
    pass

def update_record(name, record):
    pass

def delete_record(name):
    pass