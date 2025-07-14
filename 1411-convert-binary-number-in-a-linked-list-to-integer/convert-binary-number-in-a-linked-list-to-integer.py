# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        
        cur=head
        res=''
        while cur:
            res+=str(cur.val)
            cur=cur.next

        return int(res,2)

