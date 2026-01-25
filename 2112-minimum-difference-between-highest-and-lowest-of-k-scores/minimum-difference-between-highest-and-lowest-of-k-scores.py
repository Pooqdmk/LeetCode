class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        mn = 10**60
        for i in range(0,len(nums)-k+1):
            mn = min(mn, nums[i+k-1] - nums[i])
        return mn