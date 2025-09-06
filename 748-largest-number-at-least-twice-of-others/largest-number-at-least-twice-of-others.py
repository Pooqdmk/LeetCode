class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        n = sorted(nums)

        mx= n[-1]
        for i in range(len(nums)-1):
            if mx < 2*n[i]:
                return -1
        return nums.index(mx)