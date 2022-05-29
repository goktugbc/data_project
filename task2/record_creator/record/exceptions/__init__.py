class WrongFormatException(Exception):
    """
    Exception raised for doing an operation on a record with wrong data format
    """

    def __init__(self, message="Wrong format!"):
        self.message = message
        super().__init__(self.message)
