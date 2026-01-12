class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        res = 0

        for i in range(len(points)-1):
            p1,p2 = points[i], points[i+1]
            res+=max(abs(p1[0]-p2[0]), abs(p1[1]-p2[1]))
        return res
