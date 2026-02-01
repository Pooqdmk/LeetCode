class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        e = nums[0]
        s=e
        nums.sort()
        if nums[0] != e:
            s+=nums[0]
        else:
            s+=nums[1]+nums[2]
            return s
        if nums[1]!= e:
            s+=nums[1]
        else:
            s+=nums[2]
        return s