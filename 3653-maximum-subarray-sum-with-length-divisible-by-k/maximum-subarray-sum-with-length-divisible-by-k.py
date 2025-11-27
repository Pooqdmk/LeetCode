class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        res = [10**60]*k
        res[0]=0
        mx = -10**60
        s = 0
        for i in range(len(nums)):
            s+=nums[i]
            mx = max(mx,s-res[(i+1)%k])
            res[(i+1)%k] = min(res[(i+1)%k],s)
        return mx