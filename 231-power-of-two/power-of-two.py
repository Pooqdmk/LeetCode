class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n>0 and 2**floor(log(n,2)) == n:
            return True
        return False