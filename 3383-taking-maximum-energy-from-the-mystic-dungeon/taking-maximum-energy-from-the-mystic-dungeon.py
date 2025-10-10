class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = [0]*(n+k)

        for i in range(n-1,-1,-1):
            dp[i] = dp[i+k] + energy[i]
        
        return max(dp[:-k])
        