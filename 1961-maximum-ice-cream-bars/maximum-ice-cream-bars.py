class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        s = 0
        res = 0
        for i in costs:
            s+=i
            if s <= coins:
                res+=1
        return res
