class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        p = 1
        zero = 0
        for i in nums:
            if i == 0:
                zero+=1
            else:
                p*=i
            prod*=i
        res = []
        for i in nums:
            if i == 0 and zero == 1:
                res.append(p)
            elif i == 0 and zero > 1:
                res.append(0)
            else:
                res.append(prod//i)
        return res
        