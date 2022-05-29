class UnsupportedFormatException(Exception):
    """
    Exception raised for creating a record with an unsupported format
    """

    def __init__(self, message="Format is not supported."):
        self.message = message
        super().__init__(self.message)


class UnsupportedStorageTypeException(Exception):
    """
    Exception raised for getting/creating a storage with an unsupported type
    """

    def __init__(self, message="Storage type is not supported."):
        self.message = message
        super().__init__(self.message)
