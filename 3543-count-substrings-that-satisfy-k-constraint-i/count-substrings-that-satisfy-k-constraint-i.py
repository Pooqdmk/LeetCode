class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        
        # return z<=k or o<=k
        cnt=0
        n=len(s)
        for i in range(n):
            for j in range(i+1,n+1):
                l=s[i:j]
                if l:
                    z,o=l.count('0'),l.count('1')
                    if z<=k or o<=k:
                        cnt+=1
        return cnt
