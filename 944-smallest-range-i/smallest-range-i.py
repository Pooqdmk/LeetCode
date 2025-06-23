class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        
        if len(nums)==1:
            return 0
        
        nums.sort()
        mn=(nums[-1]-k) - (nums[0]+k)
        if mn>0:
            return mn
        else:
            return 0
