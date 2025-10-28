class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        r = sum(nums)
        l = 0
        res=0
        for i in range(len(nums)):
            l+=nums[i]
            r-=nums[i]
            if nums[i] == 0:
                if l == r:
                    res+=2
                elif abs(l-r) == 1:
                    res+=1
        return res
