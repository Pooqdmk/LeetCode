class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(n):
            dp[1][i+1] = dp[1][i]+grid[0][i]
        
        for j in range(m):
            dp[j+1][1] = dp[j][1] + grid[j][0]
        
        for i in range(2,m+1):
            for j in range(2,n+1):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i-1][j-1]
        return dp[-1][-1]