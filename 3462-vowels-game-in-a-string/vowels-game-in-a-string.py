class Solution:
    def doesAliceWin(self, s: str) -> bool:
        
        n=0
        for i in s:
            if i.lower() in set('aeiou'):
                n+=1
        
        if n==0:
            return False
        return True