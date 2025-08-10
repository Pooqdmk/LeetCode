class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        r1=[1]
        if x!=1:
            i=1            
            while x**i <= bound:
                r1.append(x**i)
                i+=1
        r2=[1]
        if y!=1:
            i=1
            
            while y**i <= bound:
                r2.append(y**i)
                i+=1
        res=set()
        for j in range(len(r1)):
            for k in range(len(r2)):
                s=r1[j]+r2[k]
                if s <= bound and s not in res:
                    res.add(s)
        return list(res)


