class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)

def copy_stack(original_stack):
    temp_stack = Stack()
    copy = Stack()

    while not original_stack.is_empty():
        temp_stack.push(original_stack.pop())

    while not temp_stack.is_empty():
        value = temp_stack.pop()
        original_stack.push(value)
        copy.push(value)

    return copy

stack1 = Stack()
for item in ['A', 'B', 'C', 'D']:
    stack1.push(item)

print("Original Stack:", stack1)
stack_copy = copy_stack(stack1)
print("Copied Stack:  ", stack_copy)
print("Original Stack after copy:", stack1)