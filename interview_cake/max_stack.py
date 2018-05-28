class Stack:
    # initialize an empty list
    def __init__(self):
        self.items = []

    # push a new item to the last index
    def push(self, item):
        self.items.append(item)

    # remove the last item
    def pop(self):
        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None
        return self.items.pop()

    # see what the last item is
    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

class Max_Stack:

    def __init__(self):
        self.stack = Stack()
        self.max = Stack()

    def push(self, item):
        self.stack.push(item)
        if self.max.peek() is None:
            self.max.push(item)
        else:
            if self.max.peek() <= item:
                self.max.push(item)

    def get_max(self):
        return self.max.peek()

    def pop(self):
        if self.get_max() == self.stack.peek():
            self.max.pop()
        return self.stack.pop()

    def peek(self):
        return self.stack.peek()