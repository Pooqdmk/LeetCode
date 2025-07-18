class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum=sum(nums[:k])
        mx=window_sum
        for i in range(k,len(nums)):
            window_sum+=nums[i]-nums[i-k]
            mx=max(mx,window_sum)
            

        return mx/k