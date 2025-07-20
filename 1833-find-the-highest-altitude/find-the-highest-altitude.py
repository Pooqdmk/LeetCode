class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n=len(gain)
        res=[0]*(n+1)

        for i in range(n):
            res[i+1]=gain[i]+res[i]
        return max(res)