# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1,s2 = [],[]
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        rem = 0
        s3 = []
        while s1 or s2:
            a,b = 0,0
            if s1:
                a = s1.pop() 
            if s2:
                b = s2.pop() 
            n = a+b+rem
            rem = n//10
            s3.append(n%10)
        
        if rem > 0:
            s3.append(rem)
        
        l = ListNode()
        cur = l
        while cur and s3:
            newNode = ListNode(s3.pop())
            cur.next = newNode
            cur = cur.next
        
        return l.next

        
        
