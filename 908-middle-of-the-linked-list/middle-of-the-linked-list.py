# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        cnt = 0
        while cur:
            cnt+=1
            cur = cur.next
        mid = cnt//2

        cur = head
        c = 0
        while cur:
            if c == mid:
                return cur
            c+=1
            cur = cur.next

            
        