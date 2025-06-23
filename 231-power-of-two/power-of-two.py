class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        m=math.log(n,2)
        return 2**round(m) == n
            
        