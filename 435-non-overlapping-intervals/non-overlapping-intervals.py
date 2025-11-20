class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        left,right = 0,1
        res = 0
        while right < len(intervals):
            if intervals[left][1] > intervals[right][0]:
                res+=1
            else:
                left=right
            right+=1
        return res
