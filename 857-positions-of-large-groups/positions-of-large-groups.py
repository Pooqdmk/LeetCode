class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        i=0
        cnt=1
        res=[]
        while i<len(s)-1:
            if s[i]==s[i+1]:
                cnt+=1
            else:
                if cnt>=3:
                    res.append([i-cnt+1,i])
                cnt=1
            i+=1

        if cnt >= 3:
            res.append([i-cnt+1,i])

        return res



