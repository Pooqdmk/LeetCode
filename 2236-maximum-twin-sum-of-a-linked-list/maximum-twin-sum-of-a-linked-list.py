# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        cur = head
        l = []
        while cur:
            l.append(cur.val)
            cur = cur.next
        
        mx = 0
        n=len(l)
        for i in range(len(l)):
            mx = max(mx,l[i]+l[n-1-i])
        return mx

            