class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        a=abs(x-z)
        b=abs(y-z)
        if a>b:
            return 2
        elif a==b:
            return 0
        
        else:
            return 1
        