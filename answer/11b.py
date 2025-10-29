class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)

def reverse_queue(q):
    stack = Stack()
    while not q.is_empty():
        stack.push(q.dequeue())
    while not stack.is_empty():
        q.enqueue(stack.pop())

queue1 = Queue()
for item in ['A', 'B', 'C', 'D']:
    queue1.enqueue(item)

print("Original Queue:", queue1)
reverse_queue(queue1)
print("Reversed Queue:", queue1)