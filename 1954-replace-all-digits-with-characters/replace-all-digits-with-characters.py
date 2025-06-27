class Solution:
    def replaceDigits(self, s: str) -> str:
        # d={chr(i+97):i for i in range(26)}
        res=''
        i=0
        while i < len(s)-1:
            res+=s[i]
            res+=chr(ord(s[i])+int(s[i+1]))
            i+=2
        if i< len(s):
            res+=s[i]

        return res