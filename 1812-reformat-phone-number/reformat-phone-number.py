class Solution:
    def reformatNumber(self, number: str) -> str:
        s=''
        for i in number:
            if i.isdigit():
                s+=i
        
        res=''
        n=len(s)
        if n % 3 == 0 or n%3 == 2:
            for i in range(0,n,3):
                res+=s[i:i+3]
                res+='-'
            res=res[:-1]
        elif n%3 == 1:
            for i in range(0,n-4,3):
                res+=s[i:i+3]
                res+='-'

            res+=s[-4:-2]+'-'
            res+=s[-2:]
        return res