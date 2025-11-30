class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        l,r = 1,n-2
        if nums[0] > nums[1] :
            return 0
        if nums[-1] > nums[-2]:
            return n-1

        while l<=r:
            if nums[l] > nums[l-1] and nums[l] > nums[l+1]:
                return l
            else:
                l+=1
            
            if nums[r] > nums[r-1] and nums[r] > nums[r+1]:
                return r
            else:
                r-=1

