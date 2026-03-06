class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        pos = -1
        for i in range(len(s)):
            if s[i] == '1' and pos > -1 and i > pos+1:
                return False
            elif s[i] == '1':
                pos = i
        return True
        