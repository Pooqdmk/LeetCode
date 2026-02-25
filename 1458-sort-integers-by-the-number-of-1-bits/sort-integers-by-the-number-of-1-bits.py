class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d = {}
        d1 = Counter(arr)
        for i in arr:
            d[i] = bin(i)[2:].count('1')
        
        l = sorted(d.items(), key = lambda x:(x[1],x[0]))
        res = []
        for i,j in l:
            while d1[i] > 0:
                res.append(i)
                d1[i]-=1
        return res