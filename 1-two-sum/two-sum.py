class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen=set(nums)
        
        for i in range(len(nums)):
            n=target - nums[i]
            if n in seen:
                m=nums.index(n)
                if i != m:
                    return [i,m]