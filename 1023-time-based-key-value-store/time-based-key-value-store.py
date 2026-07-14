class TimeMap:

    def __init__(self):
        self.d = {}
        self.l = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[(key,timestamp)] = value
        heapq.heappush(self.l[key], timestamp)
    def get(self, key: str, timestamp: int) -> str:
        res = self.l[key]
        t = bisect.bisect_right(res, timestamp)
        if t > -1 and t < len(res) and res[t] <= timestamp:
            return self.d[(key, res[t-1])]
        elif t-1 > -1 and t-1 < len(res) and res[t-1] <= timestamp:
            return self.d[(key, res[t-1])]
        else:
            return ""
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)