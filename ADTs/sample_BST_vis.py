import ADT_visualizers
from BinarySearchTree import BinarySearchTree

if __name__ == "__main__":
    print("Creating a very short tree...")
    # create a tree of integers containing exactly 1 value, the 5
    simple = BinarySearchTree[int](5)
    ADT_visualizers.draw_BST(simple, title="A very short tree", filename="short.gv", view = False)
    print("Adding some elements to it...")
    simple.insert(9)
    simple.insert(-3)
    ADT_visualizers.draw_BST(simple, title="A slightly taller tree", filename="taller.gv", view = False)
    
    print("Creating another tree from a list of values...")
    # create a list of values to put into the tree
    keys = [5, 1, 3, 7, 4, 6, 8, 10, 9] 
    # now build the tree based on the above list
    my_tree = BinarySearchTree[int](keys)
    ADT_visualizers.draw_BST(my_tree, title="A tree with all elements", filename="full tree.gv", view = False)

    print("Checking for values in the latest tree.")
    if my_tree.contains(10):
        print("Yippe it's there.")
    else:
        print("Nope, not there")
        
    it_is_there = 91 in my_tree
    print(f"91 is there is? {it_is_there}")

    print("Deleting a value from the tree...")
    # now delete one of the nodes
    my_tree.delete(7)
    ADT_visualizers.draw_BST(my_tree, title="A tree with 7 deleted", filename="deleted.gv", view = False)

    print("Creating a tree from a list of real numbers...")
    second_list = [3.6, 7.3, 4.1]
    real_tree = BinarySearchTree[float](second_list)
    ADT_visualizers.draw_BST(real_tree, title="A tree with real numbers", filename="reals.gv", view = False)
    showMe = real_tree.inorder([])
    print(f"Values of tree in order: {showMe}")

    print("Creating a search tree from a list of words...")
    words = ["p", "e", "a", "n", "u", "t"]
    bst3 = BinarySearchTree[str](words)
    ADT_visualizers.draw_BST(bst3, title="A tree with letters", filename="lexicographic.gv", view = False)
    
    """For fun you should try adding the following values to bst3 '9', '10', and '8'
       Did these values go where you expected them?"""