# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        o,e = [],[]
        cur = head
        c=1
        while cur:
            if c%2 == 1:
                o.append(cur.val)
            else:
                e.append(cur.val)
            c+=1
            cur = cur.next
        
        cur = head
        i = 0
        while cur and i<len(o):
            cur.val = o[i]
            i+=1
            cur = cur.next
        i=0
        while cur and i<len(e):
            cur.val = e[i]
            i+=1
            cur = cur.next
        return head