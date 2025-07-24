class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        s=sum(nums[1:])
        m=sum(nums[:1])
        res=[]
        res.append(m)
        for i in range(1,len(nums)):
            if m > s:
                return res
            m+=nums[i]
            s-=nums[i]
            res.append(nums[i])
        return res
        

