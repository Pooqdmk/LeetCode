class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=len(nums)
        cnt=0
        for i in range(1,n+1):
            if n%i == 0:
                cnt+=nums[i-1]**2
        return cnt
