class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left,right = set(),Counter(s)
        seen = set()
        for i in s:
            right[i]-=1
            
            for j in left:
                if right[j]>0:
                    seen.add((j,i))
                    
            left.add(i)
            
        return len(seen)
            