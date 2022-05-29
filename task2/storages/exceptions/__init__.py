class WrongConfigException(Exception):
    """
    Exception raised for getting wrong configuration to get storage
    """

    def __init__(self, message="Wrong config!"):
        self.message = message
        super().__init__(self.message)


class StorageOperationError(Exception):
    """
    Exception raised for not being able to do a storage operation
    """

    def __init__(self, message="Operation cannot be done."):
        self.message = message
        super().__init__(self.message)


class RecordNotFound(Exception):
    """
    Exception raised for not found record in storage
    """

    def __init__(self, message="Record not found."):
        self.message = message
        super().__init__(self.message)


class LimitOffsetIncompatibility(Exception):
    """
    Exception raised if offset value is greater than limit value
    """

    def __init__(self, message="Offset cannot be greater than limit."):
        self.message = message
        super().__init__(self.message)
