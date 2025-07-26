class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res=[]
        nums.sort()
        for i,ch in enumerate(nums):
            if ch==target:
                res.append(i)

        return res