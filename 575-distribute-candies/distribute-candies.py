class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        s=set(candyType)
        for i in range(len(s),-1,-1):
            if i<=len(candyType)/2:
                return i
