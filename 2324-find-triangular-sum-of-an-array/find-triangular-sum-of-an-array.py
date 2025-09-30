class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        dp = []
        n=len(nums)
        for i in range(n,0,-1):
            dp.append([0]*i)
        
        dp[0] = nums
        for i in range(1,len(dp)):
            for j in range(len(dp[i])):
                dp[i][j] = (dp[i-1][j] + dp[i-1][j+1])%10

        return dp[-1][0]