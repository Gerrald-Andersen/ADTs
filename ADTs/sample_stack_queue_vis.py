import ADT_visualizers
from data_structures import Stack, Queue
    
if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push(1015)
    my_stack.push(20)
    my_stack.push(30)
    my_stack.push("A")
    my_stack.push("B")

    print("Drawing stack with elements...")
    ADT_visualizers.draw_stack(my_stack, 
                               title="Stack with all elements", 
                               filename="my_stack_with_elements.gv",
                               view=False)

    my_stack.pop()
    my_stack.pop()

    print("Drawing stack after pops...")
    ADT_visualizers.draw_stack(my_stack, 
                               title="Removed top 2 elements", 
                               filename="my_stack_after_pops.gv",
                               view=False)

    empty_stack = Stack()
    print("Drawing an empty stack...")
    ADT_visualizers.draw_stack(empty_stack, 
                               filename="empty_stack.gv",
                               view = False)
    
    print("And finally with 1 element")
    empty_stack.push(17)
    ADT_visualizers.draw_stack(empty_stack, 
                               filename="one_element_stack.gv",
                               view=False)
    
    
    my_queue = Queue()
    my_queue.enqueue(10)
    my_queue.enqueue(20)
    my_queue.enqueue(30)
    my_queue.enqueue("A")
    my_queue.enqueue("B")

    print("Drawing queue with elements...")
    ADT_visualizers.draw_queue(my_queue, title="Queue with all elements", filename="my_queue_with_elements.gv", view = False)

    my_queue.dequeue()
    my_queue.dequeue()

    print("Drawing queue after removals...")
    ADT_visualizers.draw_queue(my_queue, filename="my_queue_after_pops.gv", view = False)

    empty_queue = Queue()
    print("Drawing an empty queue...")
    ADT_visualizers.draw_queue(empty_queue, filename="empty_queue.gv", view = False)
    
    print("And finally with 1 element")
    empty_queue.enqueue(17)
    ADT_visualizers.draw_queue(empty_queue, filename="one_element_queue.gv", view = False)
    