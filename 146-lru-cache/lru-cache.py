class Node:
    def __init__(self,val = 0,key = 0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = {}
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left
    def delete(self,node):
        prev,nxt = node.prev,node.next
        prev.next = nxt
        nxt.prev = prev
    def insert(self,node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node
    def get(self, key: int) -> int:
        if key in self.d:
            self.delete(self.d[key])
            self.insert(self.d[key])
            return self.d[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.delete(self.d[key])
        self.d[key] = Node(key = key,val = value)
        self.insert(self.d[key])
        if len(self.d) > self.cap:
            n_del = self.left.next
            self.delete(n_del)
            del self.d[n_del.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)