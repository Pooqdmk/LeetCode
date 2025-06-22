class Solution:
    def maxPower(self, s: str) -> int:
        cnt=0
        mx=0
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                cnt+=1
            else:
                cnt=0
            mx=max(mx,cnt)
        return mx+1
            