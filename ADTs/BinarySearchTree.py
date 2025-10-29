from typing import Optional, TypeVar, Generic
from collections.abc import Sequence
'''
BinarySearchTree stolen and adapted from
https://blog.boot.dev/computer-science/binary-search-tree-in-python/
along with Generics advice from Co-pilot
'''

T = TypeVar('T', int, float, str)  # BST treenodes must be one of int, float or maybe string

class Node(Generic[T]):
    def __init__(self, val:T) -> None:
        self.left: Optional['Node[T]'] = None
        self.right: Optional['Node[T]'] = None
        self.key: T = val

class BinarySearchTree(Generic[T]): 

    # Node class ought to be here for encapsulation sake, but...        
    
    def __init__(self, *val: T | Sequence[T]) -> None:
        """
        Creates a binary search tree using the value(s) provided.
        
        :param val: a single value or a sequence of values being all the same type
        :type val: T | Sequence[T]
        :raise
            ValueError: if not all the values in the sequence are the same type
        """
        # print("Initializing " + str(type(val)) + " with this value " + str(val))
        if val:
            # print ("init type of val is something: " + str(type(val[0])))
            # if val is list then process list
            if isinstance(val[0], Sequence):
                # print ("A list of " + str(val[0]))
                if not val:
                    self.root: Optional['Node[T]'] = None
                    self.type = None
                else:
                    self.__process_list__(val[0]) # type: ignore  # TODO: fix
            else:
                #   it's a single thing
                self.root:Optional['Node[T]'] = Node(val[0])
                self.type = type(val[0])
        else:
            self.root:Optional['Node[T]'] = None
            self.type = None
        
    def __process_list__(self, val:Sequence[T]) -> None:
        all_same_type = True
        for key in val[1:]:
            # print(type(val[0]) , type(key))
            if (type(val[0]) != type(key) and not type(key) in [int, float]):
                all_same_type = False
        if all_same_type:
            if type(val[0]) is str:
                self.root:Optional['Node[T]'] = Node[T](val[0])
            else: 
                self.root:Optional['Node[T]'] = Node[T](int(val[0]) if val[0].is_integer() else float(val[0])) # type: ignore  # TODO: fix
            self.type = type(val[0])
            for key in val[1:]:
                self.insert(key) 
                # self.insert(int(key) if key.is_integer() else float(key))
        else:
            raise ValueError("All values in the list must be the same type (e.g. integers, floats, etc.)")
    
    def insert(self, key: T) -> None:
        """
        Inserts the key into the binary search tree.  Duplicates are ignored.
        
        :param  key: the value to insert into the tree
        :type   key: T
            
        :raises
            ValueError: if the type of the key to be inserted doesn't match the type of the existing tree
        """
        if not self.type:
            self.root = Node(key)
            self.type = type(key)
        else:
            if self.type == type(key):
                self._insert_recursive(self.root, key)
            else:
                raise ValueError (f"Type of argument {type(key)} doesn't match type of tree {self.type}.")
            
    def _insert_recursive(self, tree: Node[T] | None, key: T) -> None:
        """
        Helper method to insert the key into the binary search tree.
        """
        assert(tree is not None)
        if key == tree.key:
            return
        if key < tree.key:
            if tree.left is None:
               tree.left = Node(key)
            else:
                self._insert_recursive(tree.left, key)
        else:
            if tree.right is None:
                tree.right = Node(key)
            else:
                self._insert_recursive(tree.right, key)
    
    def __contains__(self, target: T) -> bool: # do stuff that allows the in operator (key in bst) to work
        """
        Determines whether this target is somewhere in the binary search tree
        """
        return self._contains(self.root, target)
    
    def contains(self, target: T) -> bool:
        """
        Determines whether this target is somewhere in the binary search tree
        
        :param target: the target to find
        :type target: T
        :returns: whether the `target` was found or not
        :rtype: bool
        
        """
        return self._contains(self.root, target)
    
    def _contains(self, tree: Node[T] | None, target: T) -> bool:
        """
        Helper method to determine whether this target is somewhere in the binary search tree
        """
        if not tree:
            return False
        else:
            if target == tree.key:
                return True
            else:
                if target < tree.key:
                    return self._contains(tree.left, target)
                else:
                    return self._contains(tree.right, target)

    def delete(self, target: T) -> None:
        """
        Deletes the target from the binary search tree
        
        :param target: the item to delete from the tree
        :type target: `T`
        
        """
        if not self.root:
            return
        if self.root.key == target:
            # found at root
            if self.root.left and self.root.right: # case 2 children
                # more work!
                min_successor = self.root.right
                min_successor_previous = None
                while min_successor.left:
                    min_successor_previous = min_successor
                    min_successor = min_successor.left
                self.root.key = min_successor.key
                if min_successor_previous:
                    if not min_successor.right: # it is a leaf
                        min_successor_previous.left = None
                    else: 
                        min_successor_previous.left = min_successor.right
                else:
                    if not min_successor.right: # it is a leaf
                        self.root.right = None
                    else:
                        self.root.right = min_successor.right                               
                
            elif self.root.left and not self.root.right: # case left child only
                self.root = self.root.left
            elif not self.root.left and self.root.right: # case right child only
                self.root = self.root.right
            else:
                self.root = None
                self.type = None
        else:
            if self.root.key > target:
                self._delete_recursive(self.root.left, self.root, target)
            else:
                self._delete_recursive(self.root.right, self.root, target)
        
    def _delete_recursive(self, tree: Node[T] | None, previous: Node, target: T) -> None:
        if tree is None:
            return  # not found; nothing to do
        elif tree.key > target:
            self._delete_recursive(tree.left, tree, target)
            return 
        elif tree.key < target:
            tree.right = self._delete_recursive(tree.right, tree, target)
            return 
        else: # tree.key == target:
            if tree.left and tree.right: # two children
                # find min successor 
                min_successor = tree.right
                min_successor_previous = None
                while min_successor.left:
                    min_successor_previous = min_successor
                    min_successor = min_successor.left
                tree.key = min_successor.key
                # clean up where copied key came from
                if min_successor_previous:
                    if not min_successor.right: # it is a leaf
                        min_successor_previous.left = None
                    else: 
                        min_successor_previous.left = min_successor.right
                else:
                    if not min_successor.right: # it is a leaf
                        tree.right = None
                    else:
                        tree.right = min_successor.right               
            elif tree.left and not tree.right: # one child
                if previous.left and previous.left is tree:
                    previous.left = tree.left
                else:
                    previous.right = tree.left
            elif tree.right and not tree.left:
                if previous.left and previous.left is tree:
                    previous.left = tree.right
                else:
                    previous.right = tree.right
            else: # no children
                if previous.left and previous.left is tree:
                    previous.left = None
                else:
                    previous.right = None
            # found it
            # case 1: leaf
            # case 2: only 1 child
            # case 3: two children

    def inorder(self, vals: list) -> list[T]:
        """
        Produces an inorder traversal of the binary search tree, visiting each node, appending
        each value onto `vals`
        
        :param vals: a (usually empty) list
        :type vals: list
        :returns: a list of `T` with each value added in order
        :rtype: `list[T]`
        """
        if self.root:
            self._inorder_recursive(self.root, vals)
        return vals

    def _inorder_recursive(self, tree: Node[T], vals) -> None:
        if tree.left:
            self._inorder_recursive(tree.left, vals)
        if tree.key:
            vals.append(tree.key)
        if tree.right:
            self._inorder_recursive(tree.right, vals)

"""
Other methods to consider adding:
isLeaf(value) -> bool
isRoot(value) -> bool
height() -> int
getNode(value) -> Node | None
getSubtree(value) -> Tree | None.  # readonly or clone or ?
size() -> int

"""   
"""
class BSTNode:

    def __init__(self, val=None):

        self.left = None

        self.right = None

        self.val = val


    def preorder(self, vals):

        if self.val is not None:

            vals.append(self.val)

        if self.left is not None:

            self.left.preorder(vals)

        if self.right is not None:

            self.right.preorder(vals)

        return vals



    def inorder(self, vals):

        if self.left is not None:

            self.left.inorder(vals)

        if self.val is not None:

            vals.append(self.val)

        if self.right is not None:

            self.right.inorder(vals)

        return vals



    def postorder(self, vals):

        if self.left is not None:

            self.left.postorder(vals)

        if self.right is not None:

            self.right.postorder(vals)

        if self.val is not None:

            vals.append(self.val)

        return vals
"""
