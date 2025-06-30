class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # mx=0
        # for i in range(len(nums)+1):
        #     for j in combinations(nums,i):
        #         l=list(j)
        #         if l and max(l) - min(l) == 1:
        #             mx=max(mx,len(l))

        # return mx
        mx=0
        d=Counter(nums)
        for key in d.keys():
            if key+1 in d:
                mx=max(mx,d[key] + d[key+1])
        return mx