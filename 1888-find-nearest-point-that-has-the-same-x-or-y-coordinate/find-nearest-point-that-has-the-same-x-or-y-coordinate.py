class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        mn=10**60
        index=-1
        for i,(a,b) in enumerate(points):
            if a==x or b==y:
                dist=abs(a-x) + abs(b-y)
                if dist < mn:
                    mn=dist
                    index=i

        return index
                

