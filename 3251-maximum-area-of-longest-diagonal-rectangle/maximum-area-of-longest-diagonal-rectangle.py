class Solution:
    def areaOfMaxDiagonal(self, d: List[List[int]]) -> int:
        
        mx=-1
        area=0
        for w,l in d:
            d=w*w+l*l
            a=w*l

            if mx<d:
                mx=d
                area=a
            elif mx == d:
                area=max(a,area)
        return area
