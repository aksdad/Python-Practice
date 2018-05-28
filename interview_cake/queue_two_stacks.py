class QueueTwoStacks:
    def __init__(self):
        self.in_stack = list()
        self.out_stack = list()

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if len(self.out_stack) == 0:
            while len(self.in_stack) > 0:
                item = self.in_stack.pop()
                self.out_stack.append(item)
            if len(self.out_stack) == 0:
                raise IndexError("Queue empty")

        return self.out_stack.pop()