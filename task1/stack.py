from task1.exceptions.EmptyStackException import EmptyStackException
from task1.exceptions.NullElementException import NullElementException


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    # Initializing a stack.
    # Use a dummy node, which is
    # easier for handling edge cases.
    def __init__(self):
        self.head = Node("head")
        self.size_of_stack = 0

    # String representation of the stack
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-3]

    # Get the current size of the stack
    def size(self):
        return self.size_of_stack

    # Check if the stack is empty
    def empty(self):
        return self.size_of_stack == 0

    # Get the top item of the stack
    def peek(self):

        # Sanitary check to see if we
        # are peeking an empty stack.
        if self.empty():
            raise EmptyStackException("Peeking from an empty stack")
        return self.head.next.value

    # Push a value into the stack.
    def push(self, value):
        if value is None:
            raise NullElementException()
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size_of_stack += 1

    # Remove a value from the stack and return.
    def pop(self):
        if self.empty():
            raise EmptyStackException("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size_of_stack -= 1
        return remove.value
