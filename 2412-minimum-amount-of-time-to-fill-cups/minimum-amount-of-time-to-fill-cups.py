class Solution:
    def fillCups(self, amt: List[int]) -> int:
        amt.sort(reverse=True)

        if amt[0] > amt[1]+amt[2]:
            return amt[0]

        return sum(amt)//2 + sum(amt)%2
        