class NullElementException(Exception):
    """
    Exception raised for pushing None element into a stack
    """

    def __init__(self, message="You cannot push None element into the stack!"):
        self.message = message
        super().__init__(self.message)