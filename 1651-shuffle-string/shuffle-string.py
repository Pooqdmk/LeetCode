class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        l=''
        m={indices[i]:s[i] for i in range(len(s))}
        for i in range(len(s)):
            l+=m[i]
        return l


