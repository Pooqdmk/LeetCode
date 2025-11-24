class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        cur = 0
        res = []
        for i in nums:
            cur*=2
            cur+=i
            res.append(cur%5 == 0)
        return res