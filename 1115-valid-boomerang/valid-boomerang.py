class Solution:
    def isBoomerang(self, nums: List[List[int]]) -> bool:
        area=1/2*(nums[0][0]*(nums[1][1]-nums[2][1])+nums[1][0]*(nums[2][1]-nums[0][1])+nums[2][0]*(nums[0][1]-nums[1][1]))
        if area==0:
            return False
        return True