class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        res=[]
        m=n//2
        ng,pos = -1,1
        while m>0:
            res.append(ng)
            ng-=1
            res.append(pos)
            pos+=1
            m-=1
        if n%2 == 1:
            res.append(0)
        return res
            
            
        