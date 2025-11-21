class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left,right = set(),Counter(s)
        cnt = 0
        seen = set()
        for i in range(len(s)):
            right[s[i]]-=1
            if len(left)>0:
                for j in left:
                    if j in right and right[j]>0 and j+s[i] not in seen:
                        seen.add(j+s[i])
                        cnt+=1
            left.add(s[i])
            
        return cnt
            