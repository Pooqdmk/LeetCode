class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        d = [1]*n

        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                if nums[i] < nums[j]:
                    d[i] = max(d[i], 1+d[j])
                # else:
                #     d[i] = max(d[i], d[j])
        return max(d) 


