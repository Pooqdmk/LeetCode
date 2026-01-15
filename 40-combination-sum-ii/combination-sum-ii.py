class Solution:
    def combinationSum2(self, c: List[int], target: int) -> List[List[int]]:
        
        c.sort()
        res, sol = [],[]
        n = len(c)
        def dfs(i,cur_sum):
            if cur_sum == target:
                res.append(sol[:])
                return 
            
            if i == n or cur_sum > target:
                return
            sol.append(c[i])
            dfs(i+1, cur_sum+c[i])
            sol.pop()

            while i+1 < n and c[i] == c[i+1]:
                i+=1
            dfs(i+1, cur_sum)
            
        dfs(0,0)
        return res
