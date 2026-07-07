class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: Node) -> bool:
    fast, slow = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    if fast != None:
        slow = slow.next

    prev = None
    curr = slow
    next = slow

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    while head and prev:
        if head.val == prev.val:
            head = head.next
            prev = prev.next
            continue
        else:
            return False

    return True




print(isPalindrome(Node(1, Node(2, Node(3, Node(2, Node(1)))))))



	