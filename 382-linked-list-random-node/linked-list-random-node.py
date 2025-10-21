# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        cur = head
        self.cnt = 0
        while cur:
            self.cnt+=1
            cur = cur.next
        

    def getRandom(self) -> int:
        r = randint(0,self.cnt-1)
        l = 0
        cur = self.head
        while cur:
            if l == r:
                return cur.val
            l+=1
            cur = cur.next
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()