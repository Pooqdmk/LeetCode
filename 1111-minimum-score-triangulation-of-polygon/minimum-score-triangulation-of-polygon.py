class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @lru_cache(None)
        def dp(i,j):
            if i+1 == j:
                return 0
            res=10**60
            for k in range(i+1,j):
                res=min(res,values[i]*values[j]*values[k]+dp(i,k)+dp(k,j))

            return res
        return dp(0,len(values)-1)