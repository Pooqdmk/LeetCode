class Solution:
    def findMin(self, nums: List[int]) -> int:
        point = 0

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                point = i+1
                break
        return nums[point]