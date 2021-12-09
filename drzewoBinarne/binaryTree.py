from typing import Any, Callable


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None

    def is_leaf(self) -> bool:
        if self.right_child is None and self.left_child is None:
            return True
        else:
            return False

    def add_left_child(self, value: Any) -> None:
        if self is None:
            return
        else:
            self.left_child = BinaryNode(value)

    def add_right_child(self, value: Any) -> None:
        if self is None:
            return
        else:
            self.right_child = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        if self is None:
            return
        if self.left_child is not None:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child is not None:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        if self is None:
            return
        if self.left_child is not None:
            self.left_child.traverse_post_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_post_order(visit)
        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        if self is None:
            return
        visit(self)
        if self.left_child is not None:
            self.left_child.traverse_pre_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_pre_order(visit)

    def __str__(self) -> str:
        return str(self.value)

    def show(self, level):
        if self.right_child is not None:
            self.right_child.show(level+1)
        print('   ' * 3 * level + ' --*', self.value)
        if self.left_child is not None:
            self.left_child.show(level+1)


class BinaryTree:
    root: BinaryNode

    def __init__(self, value: Any):
        self.root = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        if self is None:
            return
        else:
            self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        if self is None:
            return
        else:
            self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        if self is None:
            return
        else:
            self.root.traverse_pre_order(visit)

    def show(self):
        self.root.show(0)
