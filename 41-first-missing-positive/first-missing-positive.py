class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i=1
        d = Counter(nums)
        while True:
            if i not in d:
                return i
            i+=1