class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        l = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                if l == -1:
                    l = i
                elif i-l-1 < k:
                    return False
                l = i
        return True