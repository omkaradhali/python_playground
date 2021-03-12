class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


def reverse(node):
    current = node
    previous = None
    nextnode = None

    while current != None and current.next != None:
        nextnode = current.next

        current.next = previous

        previous = current
        current = nextnode
    return previous
