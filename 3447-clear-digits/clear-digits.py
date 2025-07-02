class Solution:
    def clearDigits(self, s: str) -> str:
        i=0
        while i < len(s)-1:
            if not s[i].isdigit() and s[i+1].isdigit():
                s=s[:i]+s[i+2:]
                i=0
            else:
                i+=1

        return s