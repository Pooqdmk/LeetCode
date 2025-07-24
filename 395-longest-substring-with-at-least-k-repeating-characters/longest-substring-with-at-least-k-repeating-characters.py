class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n=len(s)
        if n<k:
            return 0
        d=Counter(s)
        
        for i in range(n):
            if d[s[i]] < k:

                left=self.longestSubstring(s[:i],k)
                right=self.longestSubstring(s[i+1:],k)

                return max(left,right)

        return n


            