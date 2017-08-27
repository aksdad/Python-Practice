import math

class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


def is_balanced(root):
    max_leaf_depth = None
    stack = list()
    stack.append((root, 0))

    if root is None:
        return True

    while stack != []:
        popped = stack.pop()
        peek = popped[0]
        depth = popped[1]
        
        if peek.right is not None:
            stack.append((peek.right, depth + 1))
        if peek.left is not None:
            stack.append((peek.left, depth + 1))

        if peek.left is None and peek.right is None:
            stack.pop()
            if max_leaf_depth is None:
                max_leaf_depth = depth
            elif abs(depth - max_leaf_depth) > 1:
                # print(str(depth) + ' ' + str(max_leaf_depth))
                return False
            else:
                max_leaf_depth = max(max_leaf_depth, depth)

    return True

if __name__ == '__main__':
    root = BinaryTreeNode(1)
    left = root.insert_left(2)
    right = root.insert_right(3)
    node_2 = left
    node_3 = right
    left = node_2.insert_left(4)
    right = root.insert_right(5)
    node_4 = left
    left = node_4.insert_left(6)
    # left.insert_left(7)
    node_3.insert_right(9)
    node_3.insert_left(8)
    print(is_balanced(root))
