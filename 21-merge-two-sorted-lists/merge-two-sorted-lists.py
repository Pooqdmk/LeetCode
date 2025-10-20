# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, cur1: Optional[ListNode], cur2: Optional[ListNode]) -> Optional[ListNode]:
        l = ListNode()
        cur = l
        while cur1 and cur2:
            if cur1.val < cur2.val:
                cur.next = cur1
                cur = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur = cur2
                cur2 = cur2.next
        
        cur.next = cur1 if cur1 else cur2
        return l.next

       
        
        