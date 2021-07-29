from math import inf


def valid_bst(root):

    def recur(root, min_value, max_value):

        if root is None:
            return True

        if root.val <= min_value:
            return False

        if root.val >= max_value:
            return False

        return recur(root.left, min_value, root.val) and recur(root.right, root.val, max_value)
