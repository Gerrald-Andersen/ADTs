"""
    Working on testing various data structures
"""
from data_structures import Queue

print(
    """
        Queue testing
    """
)
q = Queue()
q.enqueue("banana")
q.enqueue("pomegranate")
q.enqueue("starfruit")
item = q.dequeue()
print(item)
if q.is_empty():
    print("Queue is empty")
else:
    print("Queue has stuff")

while not q.is_empty():
    item = q.dequeue()
    print(item, end=", ")
print()

print("After the queue has been emptied")

# Remove the comment character from the next line
# to see what happens when you pop from an empty stack.
# item = q.dequeue()

# Leftover queues in python will get cleaned
# up automatically, so there is no need to
# destroy a queue explicitly.
# q.destroy()  # not needed.

print("done testing")
