# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s=0
        index = head
        cur = head.next
        while cur:
            s+=cur.val
            if cur.val == 0:
                newNode = ListNode(val = s)
                index.next = newNode
                newNode.next = cur

                s=0
                index = cur
            cur = cur.next
        cur = head
        prev= ListNode(next = head)
        while cur:
            if cur.val == 0:
                t = cur.next
                prev.next = cur.next
                cur = t
            else:
                prev = cur
                cur = cur.next

        return head.next

