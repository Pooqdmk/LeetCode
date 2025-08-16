class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        res=[-1]*len(intervals)
        d={tuple(intervals[i]) : i for i in range(len(intervals))}
        s=sorted(intervals)

        for i in range(len(s)):
            # found=False
            for j in range(i,len(s)):
                if s[i][1] <= s[j][0]:
                    # found=True
                    res[d[tuple(s[i])]]=d[tuple(s[j])]
                    break
            
        return res

            