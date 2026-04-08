class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        
        for i in queries:
            l,r,k,v = i
            for j in range(l,r+1,k):
                nums[j]= (nums[j] *v) % (10**9 + 7)
        res = nums[0]
        for i in range(1,len(nums)):
            res^=nums[i]
        return res