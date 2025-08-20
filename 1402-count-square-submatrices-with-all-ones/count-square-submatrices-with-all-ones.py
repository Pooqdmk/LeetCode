class Solution:
    def countSquares(self, mat: List[List[int]]) -> int:
        m=len(mat)
        n=len(mat[0])

        dp=[[0 for j in range(n)] for i in range(m)]
        dp[0] = mat[0]

        for i in range(1,m):
            for j in range(n):

                dp[i][j]=mat[i][j]
                break
        
        for i in range(1,m):
            for j in range(1,n):
                if mat[i][j] == 1:
                    dp[i][j]= min(dp[i-1][j] , dp[i][j-1] , dp[i-1][j-1])+1
        cnt=0
        for i in range(m):
            cnt+=sum(dp[i])
        return cnt


