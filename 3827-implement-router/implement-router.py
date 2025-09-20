class Router:

    def __init__(self, memoryLimit: int):
        self.ml = memoryLimit
        self.d=defaultdict(deque)
        self.s=set()
        self.q=deque()
        
    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet=(source,destination,timestamp)
        if packet in self.s:
                return False
        if len(self.q) == self.ml:
            removed = self.q.popleft()
            self.s.remove(removed)
            self.d[removed[1]].popleft()

        self.q.append(packet)
        self.s.add(packet)
        self.d[destination].append(timestamp)

        return True
        

        

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.d:
            return 0
        t=self.d[destination]
        lb=bisect_left(t,startTime)
        rb=bisect_right(t,endTime)

        return rb-lb

    def forwardPacket(self) -> list[int]:
        if self.q:
            removed= self.q.popleft()
            self.s.remove(removed)
            self.d[removed[1]].popleft()

            return removed
        return []




# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)