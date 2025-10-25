# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = []
        for i in lists:
            cur = i
            while cur:
                l.append(cur.val)
                cur = cur.next
        
        l.sort()
        cur = ListNode()
        dummy = cur
        for i in l:
            newNode = ListNode(val = i)
            dummy.next = newNode
            dummy = dummy.next
        return cur.next
