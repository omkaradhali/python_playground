"""
Max depth of a binary tree is the longest root-to-leaf path. Given a binary tree, find its max depth.

"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_max_depth(root):
    if root is None:
        return 0

    return max(tree_max_depth(root.left), tree_max_depth(root.right)) + 1


def tree_max_depth_queue(root):

    stack = []
    depth = 0
    if root is None:
        return 0

    stack = [root]

    while stack:
        for _ in stack:
            current = stack.pop()

            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)

        depth += 1

    return depth
