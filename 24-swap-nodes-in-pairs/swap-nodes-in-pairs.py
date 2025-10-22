# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode(0,head)
        prev,cur =d,head
        while cur and cur.next:
            nextPair = cur.next.next
            second = cur.next
            second.next = cur
            cur.next = nextPair
            prev.next = second

            prev = cur
            cur = nextPair
        
        return d.next
