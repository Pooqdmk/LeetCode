class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n==0:
            return 0
        nums=[0]*(n+1)
        nums[1]=1
        i=2
        while i<n+1:
            if i%2==0:
                nums[i]=nums[i//2]
            else:
                nums[i]=nums[i//2]+nums[i//2+1]
            i+=1
        return max(nums)