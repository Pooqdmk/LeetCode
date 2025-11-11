class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in strs:
            z,o = i.count('0'),i.count('1')

            for j in range(m,z-1,-1):
                for k in range(n,o-1,-1):
                    dp[j][k] = max(dp[j][k],1+dp[j-z][k-o])
        return dp[m][n]
