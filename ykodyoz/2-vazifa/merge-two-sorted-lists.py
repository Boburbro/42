class ListNode:
    def __init__(self, val=0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        current.next = list1 or list2
        return head.next

r = Solution().mergeTwoLists(
    list1=ListNode(1, next=ListNode(2, next=ListNode(4))),
    list2=ListNode(1, next=ListNode(3, next=ListNode(4)))
)

while r.next != None:
    print(r.val)
    r = r.next

