class RandomizedSet:

    def __init__(self):
        # self.d = {}
        # self.arr = []
        self.seen = set()
        self.l = []
    def insert(self, val: int) -> bool:
        if val not in self.seen:
            self.seen.add(val)
            self.l.append(val)
            return True
        return False
        # if val not in self.d:
        #     self.d[val] = len(self.arr)
        #     self.arr.append(val)
        #     return True
        # return False
    def remove(self, val: int) -> bool:
        if val in self.seen:
            self.seen.remove(val)
            self.l.remove(val)
            return True
        return False
        # if val in self.d:
        #     # del self.arr[self.d[val]]
        #     self.arr.remove(val)
        #     del self.d[val]
        #     return True
        # return False
        

    def getRandom(self) -> int:
        return random.choice(self.l)
        # return random.choice(self.arr)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()