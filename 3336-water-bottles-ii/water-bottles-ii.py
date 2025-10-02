class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        full,empty = numBottles,0
        res=0

        while full>0:
            res+=full
            empty+=full
            full=0

            while empty >= numExchange:
                empty-=numExchange
                full+=1
                numExchange+=1
        return res
