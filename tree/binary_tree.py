class BinaryTree(object):

    def __init__(self, val):
        self.root = val
        self.left = None
        self.right = None

    def insert_left(self, val):

        if self.left == None:
            self.left = BinaryTree(val)
        else:
            t = BinaryTree(val)
            t.left = self.left
            self.left = t

    def insert_right(self, val):

        if self.right == None:
            self.right = BinaryTree(val)
        else:
            t = BinaryTree(val)
            t.right = self.right
            self.right = t

    def get_right_child(self):
        return self.right

    def get_left_child(self):
        return self.left

    def set_root_value(self, val):
        self.root = val

    def get_root_val(self):
        return self.root


r = BinaryTree('a')
r.insert_left('b')
print(r.get_root_val())
print(r.get_left_child())
