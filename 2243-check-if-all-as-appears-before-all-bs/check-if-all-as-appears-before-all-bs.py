class Solution:
    def checkString(self, s: str) -> bool:
        r=''.join(sorted(s))
        return s == r