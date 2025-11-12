# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p,q = [],[]

        cur = l1
        while cur:
            p.append(cur.val)
            cur = cur.next
        cur = l2
        while cur:
            q.append(cur.val)
            cur = cur.next

        res=[]
        p,q =p[::-1],q[::-1]
        rem = 0
        i,j = 0,0
        while i<len(p) and j<len(q):
            n = p[i]+q[i]+rem
            print(n)
            if n < 10:
                res.append(n)
            else:
                res.append(n%10)
            rem = n//10
            i+=1
            j+=1
        while i<len(p):
            n = p[i]+rem
            if n < 10:
                res.append(n)
            else:
                res.append(n%10)
            rem = n//10
            i+=1
        while j<len(q):
            n = q[j]+rem
            if n < 10:
                res.append(n)
            else:
                res.append(n%10)
            rem = n//10
            j+=1
        if rem > 0:
            res.append(rem)
        l = ListNode()
        cur = l
        res = res[::-1]
        k = 0
        while cur and k<len(res):
            node = ListNode(val = res[k])
            k+=1
            cur.next = node
            cur = cur.next
        
        return l.next
        
        