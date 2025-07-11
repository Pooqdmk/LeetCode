class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        l,r='',''
        for i in range(len(p)):
            if p[i]=='*':
                l+=p[:i]
                r+=p[i+1:]
                break
        i=0
        while i <= len(s)-len(l):
            if s[i:i+len(l)] == l:
                i+=len(l)
                if r in s[i:]:
                    return True
                else:
                    return False
            i+=1
        return False