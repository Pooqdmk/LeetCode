class Solution:
    def minCost(self, b1: List[int], b2: List[int]) -> int:
        d=Counter(b1)
        l=Counter(b2)
        tot=d+l

        for key,val in tot.items():
            if val%2==1:
                return -1

        e1=[]
        e2=[]
        mn=min(tot.keys())
        for i in tot:
            req=tot[i]//2
            diff=d[i]-req

            if diff>0:
                e1.extend([i]*diff)
            elif diff<0:
                e2.extend([i]*(-diff))

        e1.sort()
        e2.sort(reverse=True)

        cost=0
        for (a,b) in zip(e1,e2):
            cost+=min(min(a,b),2*mn)
        return cost

            