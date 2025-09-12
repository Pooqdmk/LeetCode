class Solution:
    def doesAliceWin(self, s: str) -> bool:
        
        n=0
        seen={'a','e','i','o','u'}
        for i in s:
            if i.lower() in seen:
                n+=1
        
        return False if n==0 else True