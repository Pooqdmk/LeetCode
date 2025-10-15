class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        res = []
        l,n=0,len(nums)
        for i in range(n-1):
            if nums[i] >= nums[i+1]:
                res.append([l,i])
                l = i+1
        res.append([l,n-1])
        mx = 1
        for i in range(len(res)-1):
            if res[i+1][0] == res[i][-1]+1:
                mx = max(mx,min(res[i][-1]-res[i][0]+1 , res[i+1][-1]-res[i+1][0]+1))
            mx = max(mx, (res[i][-1]-res[i][0]+1)//2 )
        
        mx = max(mx , (res[-1][-1]-res[-1][0]+1)//2)
        return mx