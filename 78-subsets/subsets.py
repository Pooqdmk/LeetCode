class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        n=len(nums)
        for i in range(n):
            subset=[cur+[nums[i]] for cur in res]
            res.extend(subset)
        return res        
