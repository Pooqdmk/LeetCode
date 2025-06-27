class Solution:
    def getLucky(self, s: str, k: int) -> int:
        d={chr(i+96):i for i in range(1,27)}
        res=''
        for i in s:
            res+=str(d[i])

        while k >0:
            l=[]
            for i in res:
                l.append(int(i))
            res=str(sum(l))
            k-=1
        return int(res)
