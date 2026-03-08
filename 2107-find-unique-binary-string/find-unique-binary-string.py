class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        sol = []
        seen = set(nums)
        n = len(nums[0])
        def dfs():
            if len(sol) == n :
                r= ''.join(sol[:])
                if r not in seen:
                    return r
                return None

            sol.append('0')
            res = dfs()
            sol.pop()

            if res:
                return res
            sol.append('1')
            res = dfs()
            sol.pop()
            if res:
                return res

        return dfs()
                