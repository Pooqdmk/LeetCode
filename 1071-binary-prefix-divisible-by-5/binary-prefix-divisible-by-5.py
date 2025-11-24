class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        pre = []
        res = []
        for i in nums:
            pre.append(str(i))
            if int(''.join(pre),2)%5 == 0:
                res.append(True)
            else:
                res.append(False)
        return res

