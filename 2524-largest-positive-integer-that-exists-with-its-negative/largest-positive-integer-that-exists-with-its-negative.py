class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        # mx=-1
        nums.sort(reverse=True)
        for i in nums:
            if i>0 and -i in nums:
                return i
        return -1