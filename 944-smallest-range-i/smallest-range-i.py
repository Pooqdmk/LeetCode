class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        
        if len(nums)==1:
            return 0
        
        # nums.sort()
        mn=(max(nums)-k) - (min(nums)+k)
        if mn>0:
            return mn
        else:
            return 0
