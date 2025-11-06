# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        cur = head
        while cur:
            l.append(cur.val)
            cur = cur.next
        
        d = Counter(l)
        l = []
        for k,v in d.items():
            if v == 1:
                l.append(k)


        dummy = ListNode()
        cur = dummy
        i = 0
        while cur and i < len(l):
            newNode = ListNode(val = l[i])
            i+=1
            cur.next = newNode
            cur = cur.next
        return dummy.next

        