class Solution:
    def maxSum(self, nums: List[int]) -> int:
        l=[]
        for i in nums:
            l.append(max(str(i)))
        
        m=-1

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if l[i]==l[j]:
                    m=max(m,nums[i]+nums[j])
        return m