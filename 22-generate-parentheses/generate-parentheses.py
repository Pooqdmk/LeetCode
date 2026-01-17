class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res,sol = [],[]
        
        def dfs(i,open,close):
            if i == 2*n+1:
                res.append(''.join(sol[:]))
                return
            
            if open < n:
                sol.append('(')
                dfs(i+1,open+1,close)
                sol.pop()
            if open > close:
                sol.append(')')
                dfs(i+1,open,close+1)
                sol.pop()
        dfs(1,0,0)
        return res



            