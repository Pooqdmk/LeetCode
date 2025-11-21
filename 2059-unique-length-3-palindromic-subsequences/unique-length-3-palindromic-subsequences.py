class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        right = {}
        for i in s:
            right[i] = right.get(i,0)+1
        left = set()
        cnt = 0
        seen = {}
        for i in range(len(s)):
            right[s[i]]-=1
            if len(left)>0:
                for j in left:
                    if j in right and right[j]>0 and j+s[i] not in seen:
                        seen[j+s[i]] = 1
                        cnt+=1
            left.add(s[i])
            
        return cnt
            