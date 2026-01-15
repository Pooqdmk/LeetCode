class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res,sol = [],[]

        def dfs(i, cur_sum):
            if len(sol) == k and cur_sum == n:
                res.append(sol[:])
                return 
            if i == 10 or cur_sum > n:
                return 

            dfs(i+1, cur_sum)
            
            sol.append(i)
            dfs(i+1, cur_sum+i)
            sol.pop()

        dfs(1,0)
        return res

            
