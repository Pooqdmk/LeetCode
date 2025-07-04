class Solution:
    def reformat(self, s: str) -> str:
        d,l='',''
        for i in s:
            if i.isdigit():
                d+=i
            else:
                l+=i
        n,m=len(d),len(l)
        res = ''
        if abs(m-n) > 1:
            return res
        
        if n<m:
            d,l=l,d

        for i in range(len(s)):
            if i%2 == 0:
                res+=d[i//2]
            else:
                res+=l[i//2]

        return res

            

