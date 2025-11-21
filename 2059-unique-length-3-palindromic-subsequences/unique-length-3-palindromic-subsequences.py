class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left,right = set(),Counter(s)
        seen = set()
        for i in s:
            right[i]-=1
            if len(left)>0:
                for j in left:
                    if j in right and right[j]>0 and j+i not in seen:
                        seen.add(j+i)
                        
            left.add(i)
            
        return len(seen)
            