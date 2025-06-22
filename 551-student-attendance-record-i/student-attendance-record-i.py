class Solution:
    def checkRecord(self, s: str) -> bool:
        d=Counter(s)
        if d['A'] and d['A'] >= 2:
            return False

        for i in range(len(s)-2):
            if s[i] == 'L' and s[i+1]=='L' and s[i+2]=='L':
                return False
        return True