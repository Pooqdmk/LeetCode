class Solution:
    def thousandSeparator(self, n: int) -> str:
        s=str(n)
        if len(s) <=3:
            return s
        else:
            res=''
            s=s[::-1]
            i=0
            while i<len(s):
                res+=s[i:i+3]+'.'
                i+=3
            return res[::-1].strip('.')


