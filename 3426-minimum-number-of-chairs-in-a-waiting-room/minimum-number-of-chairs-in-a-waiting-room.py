class Solution:
    def minimumChairs(self, s: str) -> int:
        
        cnt=0
        mx=-1
        for i in s:
            if i=='E':
                cnt+=1
            else:
                cnt-=1
            mx=max(mx,cnt)
        return mx