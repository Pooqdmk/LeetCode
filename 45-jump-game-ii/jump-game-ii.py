class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        j = 0
        end, far = 0,0
        for i in range(n-1):
            far = max(far, i+nums[i])
            if i == end:
                j+=1
                end = far
        return j

            