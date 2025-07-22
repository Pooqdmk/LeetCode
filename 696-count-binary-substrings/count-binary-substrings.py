class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        l=[]
        cnt=1
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                cnt+=1
            else:
                l.append(cnt)
                cnt=1
        l.append(cnt)
        res=0
        for i in range(len(l)-1):
            res+=min(l[i],l[i+1])
        return res

