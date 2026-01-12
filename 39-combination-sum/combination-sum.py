class Solution:
    def combinationSum(self, c: List[int], target: int) -> List[List[int]]:
        res,sol = [],[]
        n = len(c)
        def dfs(i, cur_sum):
            if cur_sum == target:
                res.append(sol[:])
                return
            
            if cur_sum > target or i == n:
                return
            
            dfs(i+1, cur_sum)

            sol.append(c[i])
            dfs(i, cur_sum+c[i])
            sol.pop()
        dfs(0,0)
        return res
