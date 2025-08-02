class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        d=defaultdict(list)

        for i in pick:
            d[i[0]].append(i[1])
        cnt=0
        for key,val in d.items():
            l=Counter(val)
            for k,v in l.items():
                if v>key:
                    cnt+=1
                    break
                

        return cnt