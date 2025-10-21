# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode()
        cur = d
        rem = 0
        while l1 and l2:
            cur.next = ListNode(val = (l1.val + l2.val + rem)%10)
            cur = cur.next
            rem = (l1.val + l2.val + rem) //10
            l1 = l1.next
            l2 = l2.next
        while l1:
            cur.next = ListNode(val = (l1.val+rem)%10)
            cur = cur.next
            rem = (l1.val + rem) //10
            l1 = l1.next

        while l2:
            cur.next = ListNode(val = (l2.val+rem)%10)
            cur = cur.next
            rem = (l2.val + rem) //10
            l2 = l2.next
        if rem != 0:
            cur.next = ListNode(val = rem)

        return d.next
        