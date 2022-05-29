class WrongFormatException(Exception):
    """
    Exception raised for pushing None element into a stack
    """

    def __init__(self, message="Wrong format!"):
        self.message = message
        super().__init__(self.message)
