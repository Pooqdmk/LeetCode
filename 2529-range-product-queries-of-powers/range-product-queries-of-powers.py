class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        p=[]
        b=bin(n)[2:][::-1]
        d={i:b[i] for i in range(len(b))}
        for k,v in d.items():
            if v=='1':
                p.append(2**k)
        res=[]
        for i in queries:
            r=1
            for j in range(i[0],i[1]+1):
                r*=p[j]
            res.append(r%(10**9 + 7))
        return res
            

