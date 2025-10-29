import sys
import os
sys.path.append("D:/Langara/CPSC 1050/lab/Lab 7/ADTs")

from data_structures import Stack, Queue
from BinarySearchTree import BinarySearchTree
from ADT_visualizers import (
    generate_queue_visualization,
    generate_stack_visualization,
    generate_BST_visualization,
    display_visualization
)

stack = Stack()
stack.push('A')
stack.push('B')
stack.push('C')
print("Stack after pushes:", stack._items)

stack.pop()
print("Stack after one pop:", stack._items)

generate_stack_visualization(stack, "../imgs/lab10_stack.gv")
dot_representation_stack = generate_stack_visualization(stack, "My Stack")
display_visualization(dot_representation_stack, filename="lab10_stack", format="svg", view=True)

queue = Queue()
queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')
print("Queue after enqueues:", queue._items)

queue.dequeue()
print("Queue after one dequeue:", queue._items)

generate_queue_visualization(queue, "../imgs/lab10_queue.gv")
dot_representation = generate_queue_visualization(queue, "My Queue")
display_visualization(dot_representation, filename="lab10_queue", format="svg", view=True)

bst = BinarySearchTree()
for letter in ['D', 'B', 'F', 'A', 'C', 'E', 'G']:
    bst.insert(letter)

print("In-order traversal:", bst.inorder([]))

generate_BST_visualization(bst, "../imgs/lab10_bst.gv")
dot_representation = generate_BST_visualization(bst, "My BST")
display_visualization(dot_representation, filename="lab10_bst", format="svg", view=True)