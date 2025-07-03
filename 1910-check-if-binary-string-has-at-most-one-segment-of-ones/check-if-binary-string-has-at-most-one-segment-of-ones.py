class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if len(s) == 1:
            return True
        d=Counter(s)
        if not d['1'] or d['1'] == 1:
            return True
        cnt=1
        for i in range(len(s)-1):
            if s[i] == s[i+1] == '1':
                cnt+=1
                if cnt == d['1']:
                    return True
        return False
