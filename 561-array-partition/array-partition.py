class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # nums.sort()
        # m=nums[0]
        # n=nums[len(nums)-2]
        # return m+n
        cnt=0
        nums.sort()
        for i in range(0,len(nums)-1,2):
            cnt+=min(nums[i],nums[i+1])
        return cnt

