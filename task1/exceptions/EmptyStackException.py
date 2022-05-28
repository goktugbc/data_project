class EmptyStackException(Exception):
    """
    Exception raised for getting an element from an empty stack
    """

    def __init__(self, message="The stack is empty"):
        self.message = message
        super().__init__(self.message)
