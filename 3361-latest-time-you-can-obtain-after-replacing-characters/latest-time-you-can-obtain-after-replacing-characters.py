class Solution:
    def findLatestTime(self, s: str) -> str:
        
        hh=list(s[:2])
        mm=list(s[3:])

        if hh[0] == '?':
            if hh[1] == '?' or hh[1]=='1' or hh[1]=='0':
                hh[0]='1'
            else:
                hh[0]='0'
        
        if hh[1] == '?':
            if hh[0]=='1':
                hh[1]='1'
            else:
                hh[1]='9'
        
        if mm[0]=='?':
            mm[0]='5'

        if mm[1]=='?':
            mm[1]='9'
        return ''.join(hh)+':'+''.join(mm)