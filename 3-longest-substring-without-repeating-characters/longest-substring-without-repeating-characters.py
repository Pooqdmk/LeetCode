class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        
        d = {}
        l,r = 0,0
        n = len(s)
        mx = float('-inf')
        while r < n:
            if s[r] in d and d[s[r]] == 1:
                mx = max(mx, r-l)
                while d[s[r]] == 1:
                    if s[l] == s[r]:
                        l+=1
                        break
                    d[s[l]] = 0
                    l+=1
            d[s[r]] = 1
            r+=1
        mx = max(mx, r-l)
        return mx

