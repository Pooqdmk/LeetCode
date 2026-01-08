class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res,sol =[],[]
        def dfs(i):
            if len(sol) == k:
                res.append(sol[:])
                return
            
            for j in range(i,n):
                if j+1 not in sol:
                    sol.append(j+1)
                    dfs(j+1)
                    sol.pop()
            
        dfs(0)
        return res