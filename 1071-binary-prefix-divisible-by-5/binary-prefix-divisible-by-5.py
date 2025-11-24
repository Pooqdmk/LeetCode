class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        pre = ''
        res = []
        for i in nums:
            pre+=str(i)
            if int(pre,2)%5 == 0:
                res.append(True)
            else:
                res.append(False)
        return res

