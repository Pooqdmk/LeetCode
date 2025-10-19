class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.l = [0]*n
        self.i = 0
    def insert(self, idKey: int, value: str) -> List[str]:
        self.l[idKey-1] = value
        res = []
        while self.i<self.n and self.l[self.i] != 0:
            res.append(self.l[self.i])
            self.i+=1
        return res



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)