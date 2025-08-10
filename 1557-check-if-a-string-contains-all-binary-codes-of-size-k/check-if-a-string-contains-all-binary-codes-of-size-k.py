class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        m=2**k
        seen=set()
        n=len(s)
        for i in range(0,n-k+1):
            r=s[i:i+k]
            if r not in seen:
                seen.add(r)
        return len(seen) == m
