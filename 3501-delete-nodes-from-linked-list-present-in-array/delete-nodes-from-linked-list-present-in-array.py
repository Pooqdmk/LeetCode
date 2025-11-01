# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy

        cur = head
        seen = set(nums)
        while cur:
            if cur.val not in seen:
                prev.next = ListNode(val = cur.val)
                prev = prev.next
            cur = cur.next
        return dummy.next
            