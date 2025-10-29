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

    def delete(self, value):
        self.root = self._delete_rec(self.root, value)

    def _delete_rec(self, node, value):
        if node is None:
            return None
        if value < node.value:
            node.left = self._delete_rec(node.left, value)
        elif value > node.value:
            node.right = self._delete_rec(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete_rec(node.right, temp.value)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        return self._inorder_rec(self.root)

    def _inorder_rec(self, node):
        if node is None:
            return []
        return self._inorder_rec(node.left) + [node.value] + self._inorder_rec(node.right)

bst = BST()
flowers = ['Lily', 'Rose', 'Daffodil', 'Tulip', 'Petunia']
for flower in flowers:
    bst.insert(flower)

print("In-order traversal of BST after insertion:", bst.inorder())
