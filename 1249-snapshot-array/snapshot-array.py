class SnapshotArray:

    def __init__(self, length: int):
        #[snap_id,val]
        self.l = [[[0,0]] for i in range(length)]
        self.t = 0
    def set(self, index: int, val: int) -> None:
        if self.t == self.l[index][-1][0]:
            self.l[index][-1][-1] = val
        else:
            self.l[index].append([self.t,val])

    def snap(self) -> int:
        self.t+=1
        return self.t-1

    def get(self, index: int, snap_id: int) -> int:
        t = self.l[index]
        res = [i for i,j in t]
        idx = bisect.bisect_right(res, snap_id)
        return t[idx-1][-1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)