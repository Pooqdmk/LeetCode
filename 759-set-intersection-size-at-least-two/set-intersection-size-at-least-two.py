class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:(x[-1],-x[0]))
        res = 0
        p1,p2=-1,-1

        for i,j in intervals:
            if p2 < i:
                res+=2
                p1,p2 = j-1,j
            elif p1 < i:
                res+=1
                p1,p2 = p2,j
        return res