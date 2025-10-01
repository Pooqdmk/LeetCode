class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        cnt=numBottles
        while numBottles >= numExchange:
            n=numBottles//numExchange
            cnt+= n
            numBottles =numBottles % numExchange + n
        return cnt