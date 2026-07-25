class Solution:
    def maxProduct(self, n: int) -> int:
        l = sorted(list(str(n)))
        return int(l[-1])*int(l[-2])