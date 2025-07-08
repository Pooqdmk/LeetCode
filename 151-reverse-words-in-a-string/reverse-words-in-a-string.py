class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        l=s.split()
        s=' '.join(l[::-1])
        return s

        