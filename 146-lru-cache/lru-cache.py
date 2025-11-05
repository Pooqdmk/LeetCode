class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.capacity = capacity
        self.q = deque()
        self.seen = set()
    def get(self, key: int) -> int:
        if key in self.seen:
            self.q.remove(key)
            self.q.append(key)
            return self.d[key]
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.seen:
            self.d[key] = value
            self.q.remove(key)
            
        elif self.capacity == len(self.d):
            r = self.q.popleft()
            del self.d[r] 
            self.seen.remove(r)   
        self.seen.add(key)
        self.q.append(key)
        self.d[key] = value  
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity) 
# param_1 = obj.get(key)
# obj.put(key,value)