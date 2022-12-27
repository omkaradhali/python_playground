# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode) -> ListNode:

    dummy = ListNode(0, head)
    left = dummy.next
    right = head.next

    while right:
        left.next = None
        temp = right.next
        right.next = left

        left = temp
        right = left.next

    return dummy.head






if __name__ == "__main__":
    e = ListNode(5)
    d = ListNode(4, e)
    c = ListNode(3, d)
    b = ListNode(2, c)
    a = ListNode(1, b)

    print(reverseList(a))
