class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def is_empty(self):
        return self.top is None

    def add(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        self.count += 1

    def delete(self):
        if self.is_empty():
            return "Stack is empty"
        value = self.top.value
        self.top = self.top.next
        self.count -= 1
        return value


s = Stack()
s.add(1)
s.add(2)
s.add(3)
print(s.delete())  # Output: 3
print(s.delete())  # Output: 2
print(s.delete())  # Output: 1
print(s.delete())  # Output: 1