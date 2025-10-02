class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        d={}
        d[0] = 1
        res,s=0,0
        for i in nums:
            s+=i
            res+=d.get(s-k,0)  
            d[s]=d.get(s,0)+1
        return res

