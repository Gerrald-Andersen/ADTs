import graphviz
from data_structures import Stack, Queue
from BinarySearchTree import BinarySearchTree, Node, T

def generate_queue_visualization(queue_instance:Queue, title:str="") -> str:
    """
    Generates a DOT language string representing an illustration for a given queue instance.
    Places the title on the top of the illustration.
    
    Args:
        queue_instance: An instance of the queue class
        title: The title shown on the top of this illustration
    Returns:
        str: A DOT language instance of all the items in a queue
    """
    dot = graphviz.Digraph(comment='Queue Visualization', 
                  graph_attr={'rankdir': 'BT', # BT for Bottom-Top
                              "labelloc": "t",
                              "fontsize": "24",
                              "fontname": "serif",
                              "label": title}, 
                  node_attr={'fontsize': "16",
                             "fontname": "Comic Sans MS",
                             'shape': 'rectangle'}) 

    if queue_instance.is_empty():
        dot.node('empty', 'Queue is Empty', shape='box')
    else:
        my_copy = queue_instance._items
        queue_label = " | ".join(map(str,my_copy))
        #print(queue_label)
        
        dot.node("front_label", label="Front", shape="plaintext")
        dot.node("rear_label", label="Rear", shape="plaintext")
        
        dot.node('queue', label=f"<front> {queue_label} | <rear> &nbsp;", shape='record')
        dot.edge('front_label', 'queue:front')
        dot.edge('rear_label', 'queue:rear')
        
    return dot.source

def generate_stack_visualization(stack_instance:Stack, title:str="") -> str:
    '''
    Generates a DOT language string representing an illustration for a given stack instance.
    Places the title on the top of the illustration.
    
    Args:
        stack_instance: An instance of the stack class
        title: The title shown on the top of this illustration
   Returns:
        str: A DOT language instance of all the items in a stack
    '''
    dot = graphviz.Digraph(comment='Stack Visualization', 
                  graph_attr={'rankdir': 'LR', # BT for Bottom-Top
                              "labelloc": "t",
                              "fontsize": "24",
                              "label": title}, 
                  node_attr={'fontsize': "16",
                             "fontname": "Comic Sans MS",
                             'shape': 'rectangle'}) 

    if stack_instance.is_empty():
        dot.node('empty', 'Stack is Empty', shape='box')
    else:
        my_copy = stack_instance._items.copy()
        my_copy.reverse()
        stack_label = " | ".join(map(str,my_copy))
        #print(stack_label)
        
        dot.node("top_label", label="Top", shape="plaintext")
        
        dot.node('stack', label=f"<top> {stack_label}", shape='record')
        dot.edge('top_label', 'stack:top')

    return dot.source

def generate_BST_visualization(BST_instance:BinarySearchTree, title:str="") -> str:
    """
    Generates a DOT language string representing an illustration for a given BST instance.
    Places the title on the top of the illustration.
    
    Args:
        BST_instance: An instance of the BinarySearchTree class
        title: The title shown on the top of this illustration
    Returns:
        str: A DOT language instance of all the items in a binary search tree
    """

    '''graphviz part stolen from 
    https://levelup.gitconnected.com/binary-tree-implementation-and-visualization-in-python-2f4782887ca2

    '''
    def add_fake_node(from_here: str):
        nonlocal fake
        dot.node("fake"+str(fake),"o",style="invis", width="0.1")
        dot.edge( from_here, "fake"+str(fake), "", style="invis")
        fake = fake + 1
       
    def add_nodes_edges(node: Node[T]):
        # if node.left and node.right:
        # both sides so need a fake node between
        # if node.left:
        #  only on left so need fake node in middle and right
        # if node.right:
        #  only on right so need fake node in middle and left
        if node.left and node.right:
            dot.node(str(node.left.key))
            dot.edge(str(node.key), str(node.left.key))
            add_fake_node(str(node.key)+":s")
            dot.node(str(node.right.key))
            dot.edge(str(node.key), str(node.right.key))
            add_nodes_edges(node.left)
            add_nodes_edges(node.right)
        elif node.left:
            dot.node(str(node.left.key))
            dot.edge(str(node.key), str(node.left.key))
            add_fake_node(str(node.key)+":s")   
            add_fake_node(str(node.key))   
            add_nodes_edges(node.left)
        elif node.right:
            add_fake_node(str(node.key))   
            add_fake_node(str(node.key)+":s")   
            dot.node(str(node.right.key))
            dot.edge(str(node.key), str(node.right.key))
            add_nodes_edges(node.right)

    dot = graphviz.Digraph(comment='Binary Search Tree Visualization', 
                  graph_attr={
                              "labelloc": "t",
                              "fontsize": "24",
                              "fontname": "serif",
                              "label": title}, 
                  node_attr={ #'fontsize': "16",
                             "fontname": "Comic Sans MS",
                 #            'shape': 'rectangle'
                            }
                  ) 
    
    if BST_instance.root:
        dot.node(str(BST_instance.root.key))
        fake = 1
        add_nodes_edges(BST_instance.root)
    else:
        dot.node("Empty tree")
    
    return dot.source


def display_visualization(dot_representation:str, filename="ADT_visualization.gv", format="svg", view=True):
    """
    Draws a visual representation of a stack/queue/etc. using Graphviz using the supplied filename into the subfolder imgs.

    Args:
        dot_representation: A string representation of the ADT using the DOT language
        filename: The name of the output file (e.g., "ADT_visualization.svg")
        view: If True, then the illustration will be opened automatically, otherwise it is simply saved
    """
    graph = graphviz.Source(dot_representation)
    if view:
        graph.render(filename=filename, directory="imgs", view=view, format=format) # You can change format to 'pdf', 'svg', etc.
    else:
        graph.save(filename=filename, directory="imgs")


def draw_stack(stack_instance:Stack, title:str="", filename:str="stack_visualization.gv", format:str="svg", view:bool=True) -> None:
    """
    A convenience function to draw the given stack using the title, saving it with filename and ren
    
    Args:
        stack_instance: An instance of the stack class
        title: The title shown on the top of this illustration
        filename: The name of the output file
        view: If True then the illustration will be opened automatically, otherwise it will be simply saved
    """
    dot_implementation = generate_stack_visualization(stack_instance, title)
    # print(dot_implementation)
    display_visualization(dot_implementation, filename, format, view)
    
def draw_queue(queue_instance:Queue, title:str="", filename:str="queue_visualization.gv", format:str="svg", view:bool=True) -> None:
    """
    A convenience function to draw the given queue using the title and filename
    
    Args:
        queue_instance: An instance of the queue class
        title: The title shown on the top of this illustration
        filename: The name of the output file
        view: If True then the illustration will be opened automatically, otherwise it will be simply saved
    """
    dot_implementation = generate_queue_visualization(queue_instance, title)
    # print(dot_implementation)
    display_visualization(dot_implementation, filename, format, view)

def draw_BST(BST_instance:BinarySearchTree, title:str="", filename:str="BST_visualization.gv", format:str="svg", view:bool=True) -> None:
    """
    A convenience function to draw the given binary search tree using the title and filename
    
    Args:
        BST_instance: An instance of the BinarySearchTree class
        title: The title shown on the top of this illustration
        filename: The name of the output file
        view: If True then the illustration will be opened automatically, otherwise it will be simply saved
    """
    dot_implementation = generate_BST_visualization(BST_instance, title)
    # print(dot_implementation)
    display_visualization(dot_implementation, filename, format, view)

