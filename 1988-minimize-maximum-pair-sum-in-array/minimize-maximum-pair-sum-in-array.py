class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        l,r = 0,n-1
        mx = 0
        while l < r:
            mx = max(mx, nums[l] + nums[r])
            l+=1
            r-=1
        return mx
