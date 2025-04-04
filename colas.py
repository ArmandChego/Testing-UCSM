# Ejercicio 1
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue esta vacio")
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            raise IndexError("Queue esta vacio")
        return self.items[0]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)