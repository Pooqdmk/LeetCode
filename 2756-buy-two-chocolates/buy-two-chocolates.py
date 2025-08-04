class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        d=prices[0]+prices[1]
        if d <=money:
            return money-d
        
        return money