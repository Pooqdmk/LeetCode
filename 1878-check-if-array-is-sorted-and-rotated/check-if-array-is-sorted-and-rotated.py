class Solution:
    def check(self, nums: List[int]) -> bool:
        
        s=sorted(nums)
        
        for i in range(len(nums)):
            if nums == s[i:]+s[:i]:
                return True
        return False