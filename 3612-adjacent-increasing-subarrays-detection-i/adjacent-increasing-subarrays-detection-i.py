class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        l,n=0,len(nums)
        res = []
        for i in range(n-1):
            if nums[i] >= nums[i+1]:
                res.append([l,i])
                l = i+1
        res.append([l,n-1])
        for i in range(len(res)-1):
            if (res[i+1][0] == res[i][-1]+1 and res[i][-1]-res[i][0]+1>=k and res[i+1][-1]-res[i+1][0]+1>=k ) or res[i][-1]-res[i][0]+1 >= 2*k:
                return True
        
        return False if res[-1][-1] - res[-1][0]+1 < 2*k else True