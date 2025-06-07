class Solution:
    def makeGood(self, s: str) -> str:
        # n=len(s)
        m=-1
        while(m!=len(s)):
            m=len(s)
            for i in range(len(s)-1):
                if ((s[i].islower() and s[i+1].isupper()) or (s[i].isupper() and s[i+1].islower())) and (s[i].lower()==s[i+1].lower()):
                    s=s[:i]+s[i+2:]
                    break
            # m=len(s)
        return s
                 