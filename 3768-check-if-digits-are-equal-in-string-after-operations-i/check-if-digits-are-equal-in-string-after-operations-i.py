class Solution:
    def hasSameDigits(self, s: str) -> bool:
        
        while len(s)!=2:
            res = []
            for i in range(0,len(s)-1):
                res.append(str((int(s[i])+int(s[i+1]))%10))

            s = ''.join(res)
            
        return True if s[0] == s[1] else False
                
            
