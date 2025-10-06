class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = []
        for i in s:
            if i.isalpha() or i.isdigit():
                l.append(i.lower())
        l = ''.join(l)
        return l == l[::-1]