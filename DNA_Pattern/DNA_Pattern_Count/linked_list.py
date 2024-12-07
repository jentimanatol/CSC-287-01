from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Appends a new node with the given data to the end of the linked list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def __iter__(self):
        """Allows the linked list to be iterable."""
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __len__(self):
        """Returns the length of the linked list."""
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
