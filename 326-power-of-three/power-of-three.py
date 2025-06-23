class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        m=log(n,3)
        return 3**round(m) == n