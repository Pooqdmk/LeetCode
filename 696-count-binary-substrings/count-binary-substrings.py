class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        prev=0
        cnt=1
        res=0
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                cnt+=1
            else:
                res+=min(prev,cnt)
                prev=cnt
                cnt=1
        res+=min(prev,cnt)
        return res
            