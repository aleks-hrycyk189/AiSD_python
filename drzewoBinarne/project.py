from typing import List
from binaryTree import BinaryNode
from binaryTree import BinaryTree

finish = []

def right_line(tree: BinaryTree) -> List[BinaryNode]:
    root = tree.root
    if root is None:
        return
    right_line_hel(root)
    return finish

def right_line_hel(node:BinaryNode, level=0):
    if node is None:
        return
    if level >= len(finish):
        finish.append(node.value)
        print(node.value, end=' ')

    if node.right_child is not None:
        right_line_hel(node.right_child, level + 1)
    if node.left_child is not None:
        right_line_hel(node.left_child, level + 1)



tree = BinaryTree(10)
tree.root.add_left_child(9)
tree.root.add_right_child(2)
tree.root.left_child.add_left_child(1)
tree.root.left_child.add_right_child(3)
tree.root.left_child.right_child.add_left_child(2)
tree.root.right_child.add_right_child(6)
tree.root.right_child.add_left_child(4)

print(right_line(tree))


# tree = BinaryTree(1)
# tree.root.add_left_child(2)
# tree.root.add_right_child(3)
# tree.root.left_child.add_left_child(4)
# tree.root.left_child.add_right_child(5)
# tree.root.right_child.add_right_child(7)
# tree.root.left_child.left_child.add_left_child(8)
# tree.root.left_child.left_child.add_right_child(9)
# tree.show()
# print(right_line(tree))