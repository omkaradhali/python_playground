class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


def check_cycle(node):
    cur_val = node.value

    while node.next != None:
        if node.next.value == cur_val:
            return True
        node = node.next

    return False


def check_cycle2(node):
    n1 = node
    n2 = node

    while n2 != None and n2.next != None:
        if n2.next == n1:
            return True
        n2 = n2.next

    return False


a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c
c.next = a


print(check_cycle2(c))
