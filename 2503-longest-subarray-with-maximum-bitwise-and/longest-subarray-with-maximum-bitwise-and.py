class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        elem=max(nums)
        mx=-1
        index=nums.index(elem)
        cnt=1
        for i in range(index+1,len(nums)):
            if nums[i] == elem:
                cnt+=1
            else:
                mx=max(mx,cnt)
                cnt=0
        mx=max(mx,cnt)
        return mx
