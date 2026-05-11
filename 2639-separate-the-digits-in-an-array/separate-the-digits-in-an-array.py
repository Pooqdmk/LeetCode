class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            t = str(i)
            for j in t:
                res.append(int(j))
        return res

        