class UnsupportedFormatException(Exception):
    """
    Exception raised for pushing None element into a stack
    """

    def __init__(self, message="Format is not supported."):
        self.message = message
        super().__init__(self.message)