class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(head1: Node, head2: Node) -> Node:
    head = Node()
    current = head

    while head1 and head2:
        if head1.val<head2.val:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next

        current = current.next
        
    current.next = head1 or head2
    return head.next