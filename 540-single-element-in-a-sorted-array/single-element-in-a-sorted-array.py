class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # d=Counter(nums)
        # for k,v in d.items():
        #     if v == 1:
        #         return k
        n=len(nums)
        if n==1:
            return nums[-1]
        left,right=0,n-1
        while left < right:
            if nums[left] == nums[left+1]:
                left+=2
            else:
                return nums[left]
            if nums[right] == nums[right-1]:
                right-=2
            else:
                return nums[right]
        return nums[left]