# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a = []

        cur = head
        while cur:
            a.append(cur.val)
            cur = cur.next
        n = len(a)
        if n == 0:
            return None
        k = k%n
        a = a[-k:] + a[:-k]
        i = 0
        dummy = ListNode()
        cur = dummy
        while i<n:
            newnode = ListNode(val = a[i])
            i+=1
            cur.next = newnode
            cur = cur.next
        return dummy.next
