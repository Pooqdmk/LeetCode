class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        n = sorted(nums) 
            
        return nums.index(n[-1]) if n[-1] >= 2* n[-2] else -1