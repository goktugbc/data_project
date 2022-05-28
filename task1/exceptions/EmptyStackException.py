class EmptyStackException(Exception):
    """
    Exception raised for pushing None element into a stack
    """

    def __init__(self, message="The stack is empty"):
        self.message = message
        super().__init__(self.message)