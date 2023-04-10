class Stack:
    def __init__(self):
        self.stack = []
        self.top = 0
        
    def add(self, element):
        self.stack.append(element)
        self.top += 1
        
    def delete(self):
        if self.top > 0:
            result = self.stack[self.top -1]
            del self.stack[self.top -1]
            self.top -= 1
            return result
        else:
            print("Stack is empty")


s = Stack()
s.add(1)
s.add(2)
s.add(3)
print(s.delete())  # Output: 3
print(s.delete())  # Output: 2
print(s.delete())  # Output: 1