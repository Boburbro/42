class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def lengthOf(head: Node) -> int:
    length = 0

    while head:
        length += 1
        head = head.next

    return length


def getIntersectionNode(headA: Node, headB: Node) -> Node:
    lengthA, lengthB = lengthOf(headA), lengthOf(headB)
    result = None

    diff = abs(lengthA - lengthB)
    if lengthA > lengthB:
        for _ in range(diff):
            headA = headA.next
    else:
        for _ in range(diff):
            headB = headB.next

    while headA and headB:
        if headA == headB:
            result = headA
            break
        
        headA = headA.next
        headB = headB.next

    return result
