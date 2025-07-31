class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        while k>0:
            mn=min(nums)
            i=nums.index(mn)
            nums[i]-=2*nums[i]
            k-=1

        return sum(nums)