class Solution:
    def countSegments(self, s: str) -> int:
        if s=="":
            return 0
        m=s.split(' ')
        cnt=0
        for i in m:
            if i==" " or i=="":
                continue 
            else:
                cnt+=1
        return cnt