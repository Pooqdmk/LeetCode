class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d=Counter(nums)
        for key,val in d.items():
            if val>=2:
                return True
        return False