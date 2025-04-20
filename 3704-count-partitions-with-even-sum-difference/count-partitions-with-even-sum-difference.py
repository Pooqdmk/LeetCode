class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        cnt=0
        n=len(nums)
        for i in range(n):
            if abs(sum(nums[:i+1])-sum(nums[i+1:n]))%2==0 and nums[i+1:n]!=[]:
                cnt+=1
        return cnt