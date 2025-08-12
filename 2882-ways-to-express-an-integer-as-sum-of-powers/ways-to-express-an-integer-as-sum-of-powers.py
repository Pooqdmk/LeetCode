class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        k=1
        powers=[]
        while True:
            if k**x <= n:
                powers.append(k**x)
                k+=1
            else:
                break
        dp=[0]*(n+1)
        dp[0]=1
        for i in powers:
            for j in range(n,i-1,-1):
                dp[j]=(dp[j]+dp[j-i]) % (10**9+7)
        return dp[-1]
                

            
