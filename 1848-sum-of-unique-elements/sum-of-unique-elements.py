class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d=Counter(nums)
        s=0
        for key,val in d.items():
            if val==1:
                s+=key
        return s