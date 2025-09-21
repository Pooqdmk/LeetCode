class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left,right=0,0
        s=0
        mn=10**60
        while right < len(nums):
            s+=nums[right]
            while s >=target:
                mn=min(mn,right-left+1)
                s-=nums[left]
                left+=1
            right+=1
        return mn if mn!=10**60 else 0
