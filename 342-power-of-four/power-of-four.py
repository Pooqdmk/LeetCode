class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n>0 and 4**floor(log(n,4)) == n