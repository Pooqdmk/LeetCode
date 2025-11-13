class Solution:
    def maxOperations(self, s: str) -> int:
        ones,res = 0,0
        i = 0
        while i < (len(s)):
            if s[i] == '1':
                ones+=1
                
            
            elif s[i] == '0' and i+1 < len(s) and s[i+1] == '1':
                res+=ones
            i+=1
        if s[-1] == '0':
            res+=ones
        
        return res
            

