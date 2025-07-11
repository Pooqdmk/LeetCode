class Solution:
    def minimizedStringLength(self, s: str) -> int:
        # d=Counter(s)
        # return len(d.keys())
        return len(set(s))