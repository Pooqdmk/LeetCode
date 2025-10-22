# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head) 
        d = {0:dummy}
        cur = head
        s = 0
        while cur:
            s+=cur.val
            d[s] = cur
            cur = cur.next
        
        s = 0
        cur = dummy
        while cur:
            s+=cur.val
            cur.next = d[s].next
            cur = cur.next
        
        return dummy.next