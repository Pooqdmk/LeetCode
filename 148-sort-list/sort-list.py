# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        l = []
        while cur:
            l.append(cur.val)
            cur = cur.next
        
        l.sort()
        cur = head
        i=0
        while cur:
            cur.val = l[i]
            i+=1
            cur = cur.next
        return head