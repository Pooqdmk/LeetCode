class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        cnt = 1
        res = 0
        for i in range(len(prices)-1):
            if prices[i] == prices[i+1]+1:
                cnt+=1
            else:
                res+= (cnt*(cnt+1))//2
                cnt = 1
        res+= (cnt*(cnt+1))//2
        return res

