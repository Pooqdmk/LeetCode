# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        cnt = 0
        while cur:
            cnt+=1
            cur = cur.next
        
        mid = cnt//2
        d = ListNode()
        d.next = head
        cur = d
        c = 0
        while cur:
            if c == mid:
                cur.next = cur.next.next
                break
            c+=1
            cur = cur.next
        return d.next