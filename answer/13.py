class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert_rec(self.root, value)

    def _insert_rec(self, node, value):
        if node is None:
            return BSTNode(value)
        if value < node.value:
            node.left = self._insert_rec(node.left, value)
        else:
            node.right = self._insert_rec(node.right, value)
        return node

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        if node.right:
            self.print_tree(node.right, level + 1)
        print('    ' * level + node.value)
        if node.left:
            self.print_tree(node.left, level + 1)

tree1 = BST()
for letter in ['G', 'F', 'E', 'D', 'C', 'B', 'A']:  # semua anak left
    tree1.insert(letter)

print("Tree 1: All in a straight line")
tree1.print_tree()
print("\n" + "-"*30 + "\n")

tree2 = BST()
for letter in ['D', 'C', 'B', 'A', 'E', 'F', 'G']:
    tree2.insert(letter)

print("Tree 2: Up one side and down the other")
tree2.print_tree()
print("\n" + "-"*30 + "\n")

tree3 = BST()
for letter in ['D', 'B', 'F', 'A', 'C', 'E', 'G']:
    tree3.insert(letter)

print("Tree 3: Complete tree")
tree3.print_tree()
print("\n" + "-"*30 + "\n")
