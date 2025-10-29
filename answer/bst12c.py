from bst12a import BSTNode, BST

bst = BST()

flowers = ['Lily', 'Rose', 'Daffodil', 'Tulip', 'Petunia']
for flower in flowers:
    bst.insert(flower)

bst.insert('Poppy')

print("In-order traversal after inserting Poppy:", bst.inorder())

# Yes, it goes where i Expected:
#         Lily
#        /    \
#  Daffodil     Rose
#                  \
#                 Tulip
#                /
#           Petunia
#               \
#               Poppy