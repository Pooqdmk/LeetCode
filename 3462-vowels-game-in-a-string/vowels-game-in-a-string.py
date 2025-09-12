class Solution:
    def doesAliceWin(self, s: str) -> bool:
        
        n=0
        seen={'a','e','i','o','u'}
        left,right = 0,len(s)-1
        
        while left <= right:
            if s[left] in seen:
                n+=1
            if s[right] in seen:
                n+=1
            left+=1
            right-=1
        
        return False if n==0 else True