class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt=0

        while(1):
            if len(set(nums)) == 1 and nums[0] == 0:
                return cnt
            nums=[i for i in nums if i!=0]

            mn=min(nums)
            for i in range(len(nums)):
                nums[i]-=mn
            cnt+=1