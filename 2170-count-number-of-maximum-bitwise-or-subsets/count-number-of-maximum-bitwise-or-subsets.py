class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n=len(nums)
        d={}
        subset=[]
        for i in range(n+1):
            subset.extend(combinations(nums,i))

        for i in subset:
            res=0
            for j in i:
                res|=j
            d[res]=d.get(res,0)+1

        return d[max(d.keys())]

