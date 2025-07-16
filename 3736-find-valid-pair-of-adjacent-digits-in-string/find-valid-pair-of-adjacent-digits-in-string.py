class Solution:
    def findValidPair(self, s: str) -> str:
        d=Counter(s)
        for i in range(0,len(s)-1):
            l=s[i:i+2]
            if l[0]!=l[1] and d[l[0]] == int(l[0]) and d[l[1]] == int(l[1]):
                return l

        return ''