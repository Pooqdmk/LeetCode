class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        d = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        res,sol = [],[]
        n = len(digits)

        def dfs(i):
            if i == n:
                res.append(''.join(sol[:]))
                return 

            for c in d[digits[i]]:
                sol.append(c)
                dfs(i+1)
                sol.pop()
        dfs(0)

        return res
        