# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:

    dummy = ListNode(0, head)
    left = dummy
    right = head

    while n > 0 and right:
        right = right.next
        n -= 1

    while right:
        right = right.next
        left = left.next

    left.next = left.next.next

    return dummy.next


if __name__ == "__main__":
    e = ListNode(5)
    d = ListNode(4, e)
    c = ListNode(3, d)
    b = ListNode(2, c)
    a = ListNode(1, b)

    print(removeNthFromEnd(a, 2))
