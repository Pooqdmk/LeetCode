class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        d={}
        for i in time:
            d[i%60]=d.get(i%60,0)+1
        cnt=0
        l=list(d.keys())
        for i,k in enumerate(l):
            for key in l[i:]:
                if (k+key) % 60 == 0:
                    if key!=k:
                        
                        cnt+=d[key]*d[k]
                    else:
                        n=d[key]-1
                        cnt+=n*(n+1)//2
        return cnt

                        
