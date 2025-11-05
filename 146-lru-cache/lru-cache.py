class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.capacity = capacity
        self.q = deque()
    def get(self, key: int) -> int:
        if key in self.q:
            self.q.remove(key)
            self.q.append(key)
            return self.d[key]
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key] = value
            self.q.remove(key)
            
        elif self.capacity == len(self.d):
            del self.d[self.q.popleft()]    

        self.q.append(key)
        self.d[key] = value  
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity) 
# param_1 = obj.get(key)
# obj.put(key,value)