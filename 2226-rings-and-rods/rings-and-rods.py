class Solution:
    def countPoints(self, rings: str) -> int:
        d=defaultdict(list)

        for i in range(0,len(rings),2):
            d[rings[i+1]].append(rings[i])
        
        cnt=0
        for key,val in d.items():
            if len(set(val)) == 3:
                cnt+=1
        return cnt