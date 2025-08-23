class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n=len(nums)
        res=[-1]*n
        for i in range(n):
            
            for j in range(n):
                if nums[(j+i+1) % n] > nums[i]:
                    res[i]=(nums[(j+i+1)%n])
                    break
            
        return res
