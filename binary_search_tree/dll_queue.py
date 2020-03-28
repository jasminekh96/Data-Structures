from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')

class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1
        return self.size
        # self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size < 1:
            pass
        else:
            self.size -= 1
            return self.storage.remove_from_head()
        # self.storage.remove_from_head()

    def len(self):
        return self.size
        # self.storage.length