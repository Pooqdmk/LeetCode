class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        d={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

        res=[]

        def backtrack(start,path):
            if len(digits)==len(path):
                res.append(path)
                return 
            
            letters=d[digits[start]]
            for i in letters:
                backtrack(start+1,path+i)
        
        backtrack(0,"")
        return res

