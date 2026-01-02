class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)//2
        d = Counter(nums)

        for k,v in d.items():
            if v == n:
                return k
        