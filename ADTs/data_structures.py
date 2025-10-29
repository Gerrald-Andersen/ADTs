'''
A collection of data structures: Stack and queue specifically
'''
from collections import deque


class Stack:
    '''
        Stack class
    '''
    def __init__(self):
        self._items = deque()

    def is_empty(self):
        '''
        Is the stack empty
        '''
        return len(self._items) == 0

    def push(self, item):
        '''
        Appends a new item onto the top of the stack
        '''
        self._items.append(item)

    def pop(self):
        '''
        Removes the item from the top of the stack.
        If there are no items in the stack, an error is raised
        '''
        return self._items.pop()

    def top(self):
        '''
        Returns the top item from the stack, but does not modify the stack.
        If there are no items in the stack, an error is raised
        '''
        # item = None
        # if not self.is_empty():
        item = self._items[-1]
        return item

    def _size(self):
        '''
        Returns the size of the stack
        '''
        return len(self._items)

    def _dump(self):
        print(self._items)


class Queue:
    '''
        Queue class
    '''
    def __init__(self):
        self._items = deque()

    def is_empty(self):
        '''
        Is the queue empty
        '''
        return len(self._items) == 0

    def enqueue(self, item):
        '''
        Appends a new item onto the queue
        '''
        self._items.append(item)

    def dequeue(self):
        '''
        Removes the item from the front of the queue.
        If there are no items in the queue, an error is raised
        '''
        return self._items.popleft()

    def _size(self):
        '''
        Returns the size of the queue
        '''
        return len(self._items)

    def _dump(self):
        print(self._items)
