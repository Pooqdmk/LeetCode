class Solution:
    def isHappy(self, n: int) -> bool:
        s=str(n)
        # if (len(s)==1) and int(s)==1:
        #     return True
        t=0
        seen=set()
        while(True):
            if s in seen:
                break
            else:
                seen.add(s)
            t=0
            for i in s:
                t+=int(i)**2
            s=str(t)
            if t==1:
                return True

        return False

        
     
