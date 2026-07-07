# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        next = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

r = Solution().reverseList(
    head=ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4)))),
)

while r:
    print(r.val)
    r = r.next