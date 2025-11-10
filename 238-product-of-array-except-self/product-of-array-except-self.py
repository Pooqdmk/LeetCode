class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        z = 0
        p = 1
        found = False
        for i in nums:
            if i!= 0:
                p*=i
            else:
                z+=1
                found = True
        res = []
        for i in nums:
            if (found and i!=0) or z>1:
                res.append(0)
            elif i == 0:
                res.append(p)
            else:
                res.append(p//i)
        return res
