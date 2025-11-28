class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]

        while rowIndex > 0:
            r = [1]
            for i in range(len(res)):
                if i+1 == len(res):
                    r.append(res[i])
                    continue
                r.append(res[i]+res[i+1])
            res = r
            rowIndex-=1
        return res
