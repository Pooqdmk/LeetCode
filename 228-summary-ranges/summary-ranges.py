class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        
        l = []
        init = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                if init != nums[i-1]:
                    l.append(f"{init}->{nums[i-1]}")
                else:
                    l.append(f"{nums[i-1]}")
                init = nums[i]
        
        
        if init != nums[-1]:
            l.append(f"{init}->{nums[-1]}")
        else:
            l.append(f"{nums[-1]}")
        
        return l

                