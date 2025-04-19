class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt=0
        while len(nums)>=3 and len(set(nums))!=len(nums):
                nums=nums[3:]
                cnt+=1
        if len(nums)!=0:
            if len(set(nums))!=len(nums):
                cnt+=1
        return cnt

