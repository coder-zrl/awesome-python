# Python implmentation of Stack
# filename: stack.py

class Stack:

    def __init__(self):
        self.data = []
        self.count = 0

    def __str__(self):
        return f"{self.data}"

    def __len__(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def push(self, item):
        self.data.append(item)
        self.count += 1

    def pop(self):
        assert not self.is_empty()
        self.count -= 1
        return self.data.pop()

    def peek(self):
        assert not self.is_empty()
        return self.data[-1]