class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        res=[]
        i=0
        while 2**i <= 10**9:
            res.append(2**i)
            i+=1
        
        n=str(n)
        d=Counter(n)
        for i in res:
            if Counter(str(i)) == d:
                return True
        return False