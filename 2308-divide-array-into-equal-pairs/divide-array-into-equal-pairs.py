
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums.sort()
        l=True
        for i in range(0,len(nums)-1,2):
            if nums[i]==nums[i+1]:
                l=True
            else:
                l=False
                break
        if l:
            return True
        else:
            return False