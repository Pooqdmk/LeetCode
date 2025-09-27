class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        
        # points.sort()
        # x1,y1 = points[0][0],points[0][1]
        # x3,y3 = points[-1][0] ,points[-1][1]
        # points.remove([x1,y1])
        # points.remove([x3,y3])
        # points.sort(key = lambda x : x[1],reverse = True)
        # x2,y2 = points[0][0],points[0][1]

        # return .5*abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1-y2))

        def area(p1,p2,p3):
            x1,y1 = p1
            x2,y2 = p2
            x3,y3 = p3
            return .5*abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1-y2))
        mx= 0

        for p1,p2,p3 in combinations(points,3):
            mx = max(mx, area(p1,p2,p3))
        return mx