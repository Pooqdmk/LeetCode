class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        incr = sorted(nums)
        decr=sorted(nums, reverse=True)
        return nums == incr or nums == decr
