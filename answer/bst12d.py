from bst12a import BST

bst = BST()

flowers = ['Lily', 'Rose', 'Daffodil', 'Tulip', 'Petunia', 'Poppy']
for flower in flowers:
    bst.insert(flower)

bst.delete('Rose')

print("In-order traversal after deleting Rose:", bst.inorder())

# Yes, it is still a binary tree:
#         Lily
#        /    \
#  Daffodil     Tulip
#                 /
#              Petunia   
#                  \
#                  Poppy