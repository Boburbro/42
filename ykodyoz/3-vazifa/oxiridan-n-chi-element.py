class Node:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

def lengthOf(head: Node) -> int:
    length = 0

    while head:
        length += 1
        head = head.next

    return length

def removeNthFromEnd(head: Node, n: int) -> Node:
    length = lengthOf(head)
    need = length - n

    if need == 0:
        return head.next

    current = head

    for _ in range(need - 1):
        current = current.next

    current.next = current.next.next

    return head
