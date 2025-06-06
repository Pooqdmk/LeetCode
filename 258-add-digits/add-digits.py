class Solution:
    def addDigits(self, num: int) -> int:
        s=str(num)
        cnt=0
        if len(s)==1:
            return int(s)
        while(len(s)!=1):
            cnt=0
            for i in s:
                cnt+=int(i)
            s=str(cnt)
            
        return cnt
