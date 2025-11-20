class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x:(x[0],-x[-1]))
        res = []
        p1,p2 = -1,-1
        for i,j in intervals:
            if p2 < i:
                res.append([p1,p2])
                p1,p2 = i,j
            elif p2 < j:
                p2=j
        res.append([p1,p2])
        return res[1:]
