class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        cost = 0
        init = 0
        for i in range(1,len(colors)):
            if colors[i] != colors[i-1]:
                if i-init > 1:
                    need = neededTime[init:i]
                    cost+= sum(need) - max(need)
                init = i
        if len(colors) - init > 1:
            need = neededTime[init:len(colors)]
            cost+=sum(need) - max(need)

        return cost

                    
