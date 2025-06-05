class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l=[]
        for i in range(len(candies)):
            # candies[i]+=extraCandies
            l.append(max(candies)<=candies[i]+extraCandies)
        return l
            