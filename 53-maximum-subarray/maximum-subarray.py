class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        mx= nums[0]
        for i in range(1,len(nums)):
            if nums[i] > res+nums[i]:
                res = nums[i]
            else:
                res+=nums[i]
            mx = max(res,mx)


        return mx
