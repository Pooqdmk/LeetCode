class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:(x[-1],-x[0]))
        print(intervals)
        res = 2
        p1,p2 = intervals[0][-1]-1, intervals[0][-1]  
        for i in range(1,len(intervals)):
            if p2 < intervals[i][0]:
                p1,p2 = intervals[i][-1]-1,intervals[i][-1]
                res+=2        
            elif p1<intervals[i][0]:
                p1 = p2
                p2 = intervals[i][-1]
                res+=1
        return res

