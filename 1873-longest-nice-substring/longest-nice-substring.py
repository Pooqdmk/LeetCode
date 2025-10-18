class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        mx , n= 0,len(s)
        res = ''
        for i in range(n):
            for j in range(i+1,n+1):
                if j-i+1 > mx:
                    l = set(s[i:j])
                    valid = True
                    for k in l:
                        if k.islower():
                            if k.upper() not in l:
                                valid = False
                        else:
                            if k.lower() not in l:
                                valid = False
                    if valid:
                        res = s[i:j]
                        mx = j-i+1
        return res
                    
                    