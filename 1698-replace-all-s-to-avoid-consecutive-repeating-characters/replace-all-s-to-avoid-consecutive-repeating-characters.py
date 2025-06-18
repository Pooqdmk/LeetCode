class Solution:
    def modifyString(self, s: str) -> str:
        l=list(s)
        n=len(l)
        for i in range(n):
            if l[i]=='?':
                for ch in 'abc':
                    if (i==0 or l[i-1]!=ch) and (i==n-1 or l[i+1]!=ch):
                        l[i]=ch
                        break
        return ''.join(l)
            