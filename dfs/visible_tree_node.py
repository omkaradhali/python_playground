"""
In a binary tree, a node is considered "visible" if no node on the root-to-itself path has a greater value. The root is always "visible" since there are no other nodes between the root and itself. Given a binary tree, count the number of "visible" nodes.
"""
from math import inf


def visible_tree_node(root):

    def recur(root, max_value):

        if root is None:
            return 0
        # count gets assigned zero for first iteration
        # all the child nodes will iterate on count += 1
        count = 0

        if root.val > max_value:
            count += 1

        count += recur(root.left, root.val)
        count += recur(root.right, root.val)

        return count

    return recur(root, -inf)


def visible_tree_node_queue(root):
    stack = []
    count = 0

    if root is None:
        return 0

    stack = [root]

    while stack:

        current = stack.pop()

        if current.val >= root.val:
            count += 1

        if current.left:
            stack.append(current.left)

        if current.right:
            stack.append(current.right)

    return count
