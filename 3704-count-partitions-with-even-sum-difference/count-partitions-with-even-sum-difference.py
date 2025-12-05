class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        l,r = 0,sum(nums)
        cnt = 0
        for i in range(len(nums)-1):
            l+=nums[0]
            r-=nums[0]
            if (l-r)%2 == 0:
                cnt+=1
        return cnt

