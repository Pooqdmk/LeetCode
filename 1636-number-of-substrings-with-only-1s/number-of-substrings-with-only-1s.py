class Solution:
    def numSub(self, s: str) -> int:
        l,r =0,0
        cnt = 0

        while r < len(s)-1:
            if s[r] == '1' and s[r+1] == '0':
                cnt+= (r-l+1)*(r-l+2)//2
            if s[r] == '1':
                r+=1
            else:       
                r+=1
                l = r
        if s[-1] == '1':
            cnt+= (r-l+1)*(r-l+2)//2
        return cnt% (10**9 + 7)
                