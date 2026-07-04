class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def middleNode(head: Node) -> Node:
    fast = head
    slow = head

    while fast.next != null:
        fast = fast.next
        fast = fast.next
        slow = slow.next
    
    return slow
    

