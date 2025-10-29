"""
    Working on testing various data structures
"""
from data_structures import Stack

print(
    """
        Stack testing
    """
)
s = Stack()
s.push("banana")
s.push("pomegranate")
s.push("starfruit")
item = s.pop()
print(item)
if s.is_empty():
    print("Stack is empty")
else:
    print("Stack has stuff")

print("top is:" + s.top())

while not s.is_empty():
    item = s.pop()
    print(item, end=", ")
print()

print("After the stack has been emptied")

# Remove the comment character from the next line
# to see what happens when you pop from an empty stack.
# item = s.pop()

# Leftover stacks in python will get cleaned
# up automatically, so there is no need to
# destroy a stack explicitly.
# s.destroy()  # not needed.

print("done testing")
