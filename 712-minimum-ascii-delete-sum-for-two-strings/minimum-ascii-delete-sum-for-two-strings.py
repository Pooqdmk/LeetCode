class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n,m = len(s1), len(s2)
        dp = [[0 for j in range(m+1)] for i in range(n+1)]
        
        for i in range(n-1, -1,-1):
            for j in range(m-1,-1,-1):
                if s1[i] == s2[j]:
                    dp[i][j] = ord(s1[i]) + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        print(dp)

        res = sum(ord(i) for i in s1) + sum(ord(i) for i in s2) - 2*dp[0][0]
        return res