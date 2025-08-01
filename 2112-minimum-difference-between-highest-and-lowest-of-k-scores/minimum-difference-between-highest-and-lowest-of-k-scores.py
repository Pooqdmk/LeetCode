class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        mn=10**6
        for i in range(len(nums)-k+1):
            mn=min(mn,max(nums[i:i+k])-min(nums[i:i+k]))
        return mn