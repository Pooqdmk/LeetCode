"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:return None
        d = {}
        cur = head
        while cur:
            d[cur] = Node(x = cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            d[cur].next = d[cur.next] if cur.next else None
            d[cur].random = d[cur.random] if cur.random else None

            cur = cur.next
        return d[head]