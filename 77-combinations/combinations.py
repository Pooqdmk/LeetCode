class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res, sol = [],[]

        def dfs(n):
            if len(sol) == k:
                res.append(sol[:])
                return 
            
            left = n
            need = k - len(sol) 
            if left > need:
                dfs(n-1)
            
            sol.append(n)
            dfs(n-1)
            sol.pop()
        dfs(n)
        return res
        

