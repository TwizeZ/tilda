"""
Felix Larsson
Labbpartner: Anton Kancans
DD1320 Tillämpad datalogi
Labb 8
2024-11-01
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedQ:
    def __init__(self):
        self.first = None
        self.last = None

    def isEmpty(self):
        if self.first == None:
            return True
        else:
            return False

    def enqueue(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

    def dequeue(self):
        retrieved_node = self.first.value
        self.first = self.first.next
        return retrieved_node
    

    def peek(self):
        return self.first.value