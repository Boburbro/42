class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(head1: Node, head2: Node) -> Node:
    carry = 0
    head  = Node()
    curr = head

    while head1 or head2 or carry:
        n1 = head1.val if head1 else 0
        n2 = head2.val if head2 else 0

        total = n1 + n2 + carry

        carry = total // 10

        curr.next = Node(val=total % 10)
        curr = curr.next

        if head1: head1 = head1.next
        if head2: head2 = head2.next

    return head.next
