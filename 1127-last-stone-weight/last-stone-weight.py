class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)

        while len(stones) >1:
            if stones[0] == stones[1]:
                stones[:] = stones[2:]
            else:
                stones[0] -=stones[1] 
                stones[:]=stones[:1] + stones[2:]

            stones.sort(reverse=True)
        
        return stones[0] if stones else 0
