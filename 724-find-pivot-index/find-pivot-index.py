class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left,right = 0,sum(nums)
        for i in range(len(nums)):
            if i-1>-1:
                left+=nums[i-1]
            right-=nums[i]
            if left == right:
                return i
            
        return -1    
        
        