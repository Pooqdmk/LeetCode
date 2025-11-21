class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        right = {}
        for i in s:
            right[i] = right.get(i,0)+1
        left = set()
        seen = set()
        for i in s:
            right[i]-=1
            
            for j in left:
                if right[j]>0:
                    seen.add((j,i))
                    
            left.add(i)
            
        return len(seen)
            