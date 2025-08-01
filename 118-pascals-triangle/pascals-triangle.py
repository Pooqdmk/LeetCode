class Solution:
    def generate(self, n: int) -> List[List[int]]:
        res=[[0] for i in range(n)]
        res[0]=[1]
        for i in range(1,n):
            r=[0]+res[i-1]+[0]
            l=[]
            for i in range(len(r)-1):
                l.append(r[i]+r[i+1])
            res[i]=l
        return res


                
