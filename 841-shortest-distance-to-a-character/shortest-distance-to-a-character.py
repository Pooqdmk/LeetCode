class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        l=[]

        for i in range(len(s)):
            if s[i] == c:
                l.append(i)
        res=[]
        for i in range(len(s)):
            mn=10**6
            for j in l:
                mn=min(mn,abs(i-j))
            res.append(mn)
        return res
            