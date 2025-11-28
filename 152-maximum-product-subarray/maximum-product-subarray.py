class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curmn,curmx = 1,1

        for i in nums:
            t = curmx*i
            curmx = max(curmx*i,curmn*i,i)
            curmn = min(t,curmn*i,i)
            res = max(res,curmx)
        return res



            