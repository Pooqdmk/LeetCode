class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        d = Counter(nums)
        res,sol = [],[]
        n = len(nums)

        def dfs():
            if len(sol) == n:
                res.append(sol[:])
                return 
            
            for k in d.keys():
                if d[k] > 0:
                    sol.append(k)
                    d[k]-=1
                    dfs()
                    d[k]+=1
                    sol.pop()
        dfs()
        return res
        